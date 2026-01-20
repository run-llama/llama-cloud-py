"""
ExtractedData Types for Extraction Workflows

This module provides typed wrappers for extraction workflow data,
including field metadata, citations, confidence scores, and bounding boxes.

Example Usage:
    ```python
    from llama_cloud.types.beta import ExtractedData, ExtractedFieldMetadata
    from pydantic import BaseModel


    class Person(BaseModel):
        name: str
        age: int


    # Parse extraction result into typed data
    extracted = ExtractedData.from_extraction_result(extract_run, Person, status="pending_review")

    # Access typed data and metadata
    print(extracted.data.name)  # Type-safe access
    print(extracted.field_metadata["name"].confidence)  # Field confidence
    ```
"""

from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Type,
    Tuple,
    Union,
    Generic,
    Literal,
    TypeVar,
    ClassVar,
    Optional,
    cast,
)

from pydantic import Field, BaseModel, ValidationError

from ..._compat import PYDANTIC_V1, ConfigDict, GenericModel, model_parse, get_model_fields
from ..extraction import ExtractRun

if PYDANTIC_V1:
    from pydantic import root_validator  # pyright: ignore[reportDeprecated]
else:
    from pydantic import model_validator

__all__ = [
    "BoundingBox",
    "PageDimensions",
    "FieldCitation",
    "ExtractedFieldMetadata",
    "ExtractedFieldMetaDataDict",
    "parse_extracted_field_metadata",
    "ExtractedData",
    "InvalidExtractionData",
    "calculate_overall_confidence",
]

# Type variable for extracted data (can be dict or Pydantic model)
ExtractedT = TypeVar("ExtractedT", bound=Union[BaseModel, Dict[str, Any]])

# Status types for extracted data workflow
StatusType = Union[Literal["error", "accepted", "rejected", "pending_review"], str]


class BoundingBox(BaseModel):
    """Bounding box coordinates for a citation location on a page."""

    x: float = Field(description="X coordinate of the bounding box origin")
    y: float = Field(description="Y coordinate of the bounding box origin")
    w: float = Field(description="Width of the bounding box")
    h: float = Field(description="Height of the bounding box")


class PageDimensions(BaseModel):
    """Dimensions of a page in the source document."""

    width: float = Field(description="Width of the page")
    height: float = Field(description="Height of the page")


class FieldCitation(BaseModel):
    """Citation information linking an extracted field to its source location."""

    page: Optional[int] = Field(None, description="The page number that the field occurred on")
    matching_text: Optional[str] = Field(
        None,
        description="The original text this field's value was derived from",
    )
    bounding_boxes: Optional[List[BoundingBox]] = Field(
        None,
        description="Bounding boxes indicating where the citation appears on the page",
    )
    page_dimensions: Optional[PageDimensions] = Field(
        None,
        description="Dimensions of the page containing the citation",
    )


class ExtractedFieldMetadata(BaseModel):
    """
    Metadata for an extracted data field, such as confidence, and citation information.
    """

    reasoning: Optional[str] = Field(
        None,
        description="Symbol for how the citation/confidence was derived: 'INFERRED FROM TEXT', 'VERBATIM EXTRACTION'",
    )
    confidence: Optional[float] = Field(
        None,
        description="The confidence score for the field, combined with parsing confidence if applicable",
    )
    extraction_confidence: Optional[float] = Field(
        None,
        description="The confidence score for the field based on the extracted text only",
    )
    parsing_confidence: Optional[float] = Field(
        None,
        description="The confidence score for the field based on the parsing/OCR quality",
    )
    citation: Optional[List[FieldCitation]] = Field(
        None,
        description="The citation for the field, including page number and matching text",
    )

    # Forbid unknown keys to avoid swallowing nested dicts
    if PYDANTIC_V1:

        class Config:
            extra = "forbid"
    else:
        model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")  # type: ignore[misc]


ExtractedFieldMetaDataDict = Dict[str, Union[ExtractedFieldMetadata, Dict[str, Any], List[Any]]]


def parse_extracted_field_metadata(
    field_metadata: Dict[str, Any],
) -> ExtractedFieldMetaDataDict:
    """
    Parse raw extraction metadata dict into typed ExtractedFieldMetadata objects.

    Recursively processes nested dictionaries and lists to identify and convert
    field metadata based on indicator fields (confidence, extraction_confidence, citation).

    Args:
        field_metadata: Raw metadata dict from extraction API response

    Returns:
        Dict with leaf nodes converted to ExtractedFieldMetadata where applicable
    """
    return {
        k: _parse_extracted_field_metadata_recursive(v)
        for k, v in field_metadata.items()
        if not _is_reasoning_field(k, v) and k not in _ADDITIONAL_ROOT_METADATA_FIELDS
    }


def _is_reasoning_field(field_name: str, field_value: Any) -> bool:
    # There can either be a user specified reasoning field (from the schema), or a reasoning metadata field for the
    # dict of values
    return field_name == "reasoning" and isinstance(field_value, str)


_ADDITIONAL_ROOT_METADATA_FIELDS = {"error"}


def _parse_extracted_field_metadata_recursive(
    field_value: Any,
    additional_fields: Optional[Dict[str, Any]] = None,
) -> Union[ExtractedFieldMetadata, Dict[str, Any], List[Any]]:
    """
    Parse the extracted field metadata into a dictionary of field names to field metadata.
    """
    if additional_fields is None:
        additional_fields = {}

    if isinstance(field_value, ExtractedFieldMetadata):
        # support running this multiple times
        return field_value
    elif isinstance(field_value, dict):
        field_dict = cast(Dict[str, Any], field_value)
        # reasoning explicitly excluded, as it is included next to subfields, for example
        # "dimensions.width" is a leaf, but there will still potentially be a "dimensions.reasoning"
        indicator_fields = {"confidence", "extraction_confidence", "citation"}
        if len(indicator_fields.intersection(field_dict.keys())) > 0:
            try:
                merged: Dict[str, Any] = {**field_dict, **additional_fields}
                allowed_fields = set(get_model_fields(ExtractedFieldMetadata).keys())
                merged = {k: v for k, v in merged.items() if k in allowed_fields}
                validated = model_parse(ExtractedFieldMetadata, merged)

                return validated
            except ValidationError:
                pass
        new_additional_fields: Dict[str, Any] = {k: v for k, v in field_dict.items() if _is_reasoning_field(k, v)}
        return {
            k: _parse_extracted_field_metadata_recursive(v, new_additional_fields)
            for k, v in field_dict.items()
            if not _is_reasoning_field(k, v)
        }
    elif isinstance(field_value, list):
        return [_parse_extracted_field_metadata_recursive(item) for item in cast(List[Any], field_value)]
    else:
        raise ValueError(f"Invalid field value: {field_value}. Expected ExtractedFieldMetadata, dict, or list")


def _normalize_field_metadata_value(value: Any) -> Dict[str, Any]:
    """
    Helper to normalize field_metadata in inbound data.

    Ensures any inbound representation (including JSON round-trips)
    gets normalized so nested dicts become ExtractedFieldMetadata where appropriate.
    """
    if isinstance(value, dict):
        value_dict = cast(Dict[str, Any], value)
        if "field_metadata" in value_dict and isinstance(value_dict["field_metadata"], dict):
            try:
                field_metadata_dict = cast(Dict[str, Any], value_dict["field_metadata"])
                return {
                    **value_dict,
                    "field_metadata": parse_extracted_field_metadata(field_metadata_dict),
                }
            except Exception:
                # Let pydantic surface detailed errors later rather than swallowing completely
                pass
        return value_dict
    return cast(Dict[str, Any], value)


class ExtractedData(GenericModel, Generic[ExtractedT]):
    """
    Wrapper for extracted data with workflow status tracking.

    This class is designed for extraction workflows where data goes through
    review and approval stages. It maintains both the original extracted data
    and the current state after any modifications.

    Attributes:
        original_data: The data as originally extracted from the source
        data: The current state of the data (may differ from original after edits)
        status: Current workflow status (pending_review, accepted, rejected, error)
        overall_confidence: Aggregated confidence score across all fields
        field_metadata: Per-field metadata including confidence and citations
        file_id: The LlamaCloud file ID of the source file
        file_name: The name of the source file
        file_hash: Content hash for de-duplication
        metadata: Additional application-specific metadata

    Status Workflow:
        - "pending_review": Initial state, awaiting human review
        - "accepted": Data approved and ready for use
        - "rejected": Data rejected, needs re-extraction or manual fix
        - "error": Processing error occurred

    Example:
        ```python
        # Create extracted data for review
        extracted = ExtractedData.create(
            data=person_data, status="pending_review", field_metadata={"name": ExtractedFieldMetadata(confidence=0.95)}
        )

        # Later, after review
        if extracted.status == "accepted":
            process_person(extracted.data)
        ```
    """

    original_data: ExtractedT = Field(description="The original data that was extracted from the document")
    data: ExtractedT = Field(description="The latest state of the data. Will differ if data has been updated")
    status: StatusType = Field(description="The status of the extracted data")
    overall_confidence: Optional[float] = Field(
        None,
        description="The overall confidence score for the extracted data",
    )
    field_metadata: ExtractedFieldMetaDataDict = Field(
        default_factory=dict,
        description="Per-field metadata including confidence scores and citations",
    )
    file_id: Optional[str] = Field(None, description="The ID of the file that was used to extract the data")
    file_name: Optional[str] = Field(None, description="The name of the file that was used to extract the data")
    file_hash: Optional[str] = Field(None, description="The hash of the file that was used to extract the data")
    metadata: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Additional metadata about the extracted data, such as errors, tokens, etc.",
    )

    if PYDANTIC_V1:

        @root_validator(pre=True)  # pyright: ignore[reportDeprecated,reportPossiblyUnboundVariable]
        @classmethod
        def _normalize_field_metadata_on_input(cls, value: Any) -> Dict[str, Any]:  # pyright: ignore[reportRedeclaration]
            return _normalize_field_metadata_value(value)
    else:

        @model_validator(mode="before")  # pyright: ignore[reportPossiblyUnboundVariable]
        @classmethod
        def _normalize_field_metadata_on_input(cls, value: Any) -> Dict[str, Any]:
            return _normalize_field_metadata_value(value)

    @classmethod
    def create(
        cls,
        data: ExtractedT,
        status: StatusType = "pending_review",
        field_metadata: ExtractedFieldMetaDataDict = {},
        file_id: Optional[str] = None,
        file_name: Optional[str] = None,
        file_hash: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> "ExtractedData[ExtractedT]":
        """
        Create a new ExtractedData instance with sensible defaults.

        Args:
            data: The extracted data payload
            status: Initial workflow status
            field_metadata: Optional confidence scores, citations, and other metadata for fields
            file_id: The LlamaCloud file ID of the source file
            file_name: The name of the source file
            file_hash: Content hash for de-duplication
            metadata: Arbitrary additional application-specific data

        Returns:
            New ExtractedData instance ready for storage
        """
        normalized_field_metadata = parse_extracted_field_metadata(field_metadata)
        return cls(
            original_data=data,
            data=data,
            status=status,
            field_metadata=normalized_field_metadata,
            overall_confidence=calculate_overall_confidence(normalized_field_metadata),
            file_id=file_id,
            file_name=file_name,
            file_hash=file_hash,
            metadata=metadata or {},
        )

    @classmethod
    def from_extraction_result(
        cls,
        result: ExtractRun,
        schema: Type[ExtractedT],
        file_hash: Optional[str] = None,
        file_name: Optional[str] = None,
        file_id: Optional[str] = None,
        status: StatusType = "pending_review",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> ExtractedData[ExtractedT]:
        """
        Create an ExtractedData instance from an ExtractRun API response.

        Args:
            result: The ExtractRun response from the extraction API
            schema: Pydantic model class to validate the extracted data
            file_hash: Optional content hash for de-duplication
            file_name: Override the file name from the result
            file_id: Override the file ID from the result
            status: Initial workflow status (default: "pending_review")
            metadata: Additional application-specific metadata

        Returns:
            ExtractedData instance with validated, typed data

        Raises:
            InvalidExtractionData: If the extracted data doesn't match the schema.
                The exception contains an ExtractedData[Dict] with status="error"
                and the validation error in metadata.
        """
        resolved_file_id = file_id or (result.file.id if result.file else None)
        resolved_file_name = file_name or (result.file.name if result.file else None)
        job_id = result.job_id

        # Extract field_metadata from extraction_metadata, ensuring it's a dict
        job_field_metadata: Dict[str, Any] = {}
        if result.extraction_metadata:
            raw_field_metadata = result.extraction_metadata.get("field_metadata")
            if isinstance(raw_field_metadata, dict):
                job_field_metadata = cast(Dict[str, Any], raw_field_metadata)

        errors: Optional[str] = None
        raw_errors = job_field_metadata.get("error")
        if isinstance(raw_errors, str):
            errors = raw_errors

        try:
            field_metadata = parse_extracted_field_metadata(job_field_metadata)
        except ValidationError:
            field_metadata = {}

        try:
            # schema is expected to be a Pydantic model class
            data: ExtractedT = model_parse(schema, result.data)  # type: ignore[union-attr, attr-defined, assignment, type-var]
            return cls.create(
                data=data,  # pyright: ignore[reportUnknownArgumentType]
                status=status,
                field_metadata=job_field_metadata,
                file_id=resolved_file_id,
                file_name=resolved_file_name,
                file_hash=file_hash,
                metadata={
                    **({"field_errors": errors} if errors else {}),
                    "job_id": job_id,
                    **(metadata or {}),
                },
            )
        except ValidationError as e:
            raw_data: Dict[str, Any] = {}
            if isinstance(result.data, dict):
                raw_data = cast(Dict[str, Any], result.data)
            invalid_item: ExtractedData[Dict[str, Any]] = ExtractedData[Dict[str, Any]].create(
                data=raw_data,
                status="error",
                field_metadata=field_metadata,
                metadata={"extraction_error": str(e), **(metadata or {})},
                file_id=resolved_file_id,
                file_name=resolved_file_name,
                file_hash=file_hash,
            )
            raise InvalidExtractionData(invalid_item) from e


class InvalidExtractionData(Exception):
    """
    Exception raised when the extracted data does not conform to the schema.

    Contains an ExtractedData[Dict] instance with the raw data and error details
    in the metadata field.
    """

    def __init__(self, invalid_item: ExtractedData[Dict[str, Any]]):
        self.invalid_item = invalid_item
        super().__init__("Not able to parse the extracted data, parsed invalid format")


def calculate_overall_confidence(
    metadata: ExtractedFieldMetaDataDict,
) -> Optional[float]:
    """
    Calculate the overall confidence score for extracted data.

    Computes the arithmetic mean of all confidence scores found in the
    field metadata structure, recursively traversing nested dicts and lists.

    Args:
        metadata: Field metadata dict with nested ExtractedFieldMetadata objects

    Returns:
        Average confidence score, or None if no confidence values found
    """
    numerator, denominator = _calculate_overall_confidence_recursive(metadata)
    if denominator == 0:
        return None
    return numerator / denominator


def _calculate_overall_confidence_recursive(
    confidence: Union[ExtractedFieldMetadata, Dict[str, Any], List[Any], Any],
) -> Tuple[float, int]:
    """
    Recursively calculate sum and count of confidence scores.
    """
    if isinstance(confidence, ExtractedFieldMetadata):
        if confidence.confidence is not None:
            return confidence.confidence, 1
        else:
            return 0.0, 0
    if isinstance(confidence, dict):
        conf_dict = cast(Dict[str, Any], confidence)
        numerator: float = 0.0
        denominator: int = 0
        for value in conf_dict.values():
            num, den = _calculate_overall_confidence_recursive(value)
            numerator += num
            denominator += den
        return numerator, denominator
    if isinstance(confidence, list):
        conf_list = cast(List[Any], confidence)
        numerator = 0.0
        denominator = 0
        for value in conf_list:
            num, den = _calculate_overall_confidence_recursive(value)
            numerator += num
            denominator += den
        return numerator, denominator
    return 0.0, 0
