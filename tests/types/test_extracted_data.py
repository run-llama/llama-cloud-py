# pyright: reportCallIssue=false, reportUnknownMemberType=false, reportUnknownVariableType=false, reportUnknownArgumentType=false
"""Tests for ExtractedData types and helper functions."""

import json
import uuid
from typing import Any, Dict, Optional
from pathlib import Path

import pytest
from pydantic import Field, BaseModel

from llama_cloud._compat import model_json, model_parse
from llama_cloud.types.file import File
from llama_cloud.types.extraction import ExtractRun
from llama_cloud.types.beta.extracted_data import (
    BoundingBox,
    ExtractedData,
    FieldCitation,
    PageDimensions,
    InvalidExtractionData,
    ExtractedFieldMetadata,
    calculate_overall_confidence,
    parse_extracted_field_metadata,
)


# Test data models
class Person(BaseModel):
    name: str
    age: Optional[int] = None
    email: Optional[str] = None


class Company(BaseModel):
    name: str
    industry: str
    employees: int


def test_extracted_data_create_method():
    """Test ExtractedData.create class method."""
    person = Person(name="Created Person", age=35, email="created@example.com")

    # Test with defaults
    extracted = ExtractedData.create(person)
    assert extracted.original_data == person
    assert extracted.data == person
    assert extracted.status == "pending_review"
    assert extracted.field_metadata == {}
    assert extracted.overall_confidence is None

    # Test with custom values using ExtractedFieldMetadata
    field_metadata: Dict[str, Any] = {
        "name": ExtractedFieldMetadata(confidence=0.99, citation=[FieldCitation(page=1)]),
        "age": ExtractedFieldMetadata(confidence=0.85, citation=[FieldCitation(page=1)]),
    }
    extracted_custom = ExtractedData.create(person, status="accepted", field_metadata=field_metadata)
    assert extracted_custom.status == "accepted"
    name_meta = extracted_custom.field_metadata["name"]
    age_meta = extracted_custom.field_metadata["age"]
    assert isinstance(name_meta, ExtractedFieldMetadata)
    assert isinstance(age_meta, ExtractedFieldMetadata)
    assert name_meta.confidence == 0.99
    assert age_meta.confidence == 0.85
    assert extracted_custom.overall_confidence == pytest.approx((0.99 + 0.85) / 2)


def test_extracted_data_with_dict():
    """Test ExtractedData with dict data instead of Pydantic model."""
    data_dict: Dict[str, Any] = {"name": "Dict Person", "age": 45, "email": "dict@example.com"}

    extracted = ExtractedData[Dict[str, Any]](
        original_data=data_dict,
        data=data_dict,
        status="accepted",
    )

    assert extracted.original_data["name"] == "Dict Person"
    assert extracted.data["age"] == 45


def test_calculate_overall_confidence_simple_flat():
    """Test calculate_overall_confidence with simple flat dictionary of ExtractedFieldMetadata."""
    field_metadata: Dict[str, Any] = {
        "name": ExtractedFieldMetadata(confidence=0.9),
        "age": ExtractedFieldMetadata(confidence=0.8),
        "email": ExtractedFieldMetadata(confidence=0.95),
    }
    result = calculate_overall_confidence(field_metadata)
    expected = (0.9 + 0.8 + 0.95) / 3
    assert result == pytest.approx(expected, rel=1e-9)


def test_calculate_overall_confidence_nested():
    """Test calculate_overall_confidence with nested dictionary structure."""
    field_metadata: Dict[str, Any] = {
        "person": {
            "name": ExtractedFieldMetadata(confidence=0.9),
            "age": ExtractedFieldMetadata(confidence=0.8),
        },
        "contact": {
            "email": ExtractedFieldMetadata(confidence=0.95),
            "phone": ExtractedFieldMetadata(confidence=0.85),
        },
        "score": ExtractedFieldMetadata(confidence=0.7),
    }
    result = calculate_overall_confidence(field_metadata)
    expected = (0.9 + 0.8 + 0.95 + 0.85 + 0.7) / 5
    assert result == pytest.approx(expected, rel=1e-9)


def test_calculate_overall_confidence_with_lists():
    """Test calculate_overall_confidence with lists of ExtractedFieldMetadata and nested structures."""
    field_metadata: Dict[str, Any] = {
        "scores": [
            ExtractedFieldMetadata(confidence=0.9),
            ExtractedFieldMetadata(confidence=0.8),
            ExtractedFieldMetadata(confidence=0.95),
        ],
        "nested_data": [
            {
                "field1": ExtractedFieldMetadata(confidence=0.7),
                "field2": ExtractedFieldMetadata(confidence=0.6),
            },
            {
                "field1": ExtractedFieldMetadata(confidence=0.8),
                "field2": ExtractedFieldMetadata(confidence=0.9),
            },
        ],
        "single_value": ExtractedFieldMetadata(confidence=0.85),
    }
    result = calculate_overall_confidence(field_metadata)
    expected = (0.9 + 0.8 + 0.95 + 0.7 + 0.6 + 0.8 + 0.9 + 0.85) / 8
    assert result == pytest.approx(expected, rel=1e-9)


def test_calculate_overall_confidence_invalid_types():
    """Test calculate_overall_confidence with invalid/mixed types alongside valid ExtractedFieldMetadata."""
    field_metadata: Dict[str, Any] = {
        "valid_metadata": ExtractedFieldMetadata(confidence=0.8),
        "valid_metadata_no_confidence": ExtractedFieldMetadata(),
        "valid_list": [
            ExtractedFieldMetadata(confidence=0.5),
            ExtractedFieldMetadata(confidence=0.6),
        ],
        "invalid_string": "not_a_number",
        "invalid_list_mixed": [
            ExtractedFieldMetadata(confidence=0.7),
            "invalid",
            ExtractedFieldMetadata(confidence=0.8),
        ],
        "invalid_none": None,
        "random_dict": {"a": 1, "b": 2},
    }
    result = calculate_overall_confidence(field_metadata)
    expected = (0.8 + 0.5 + 0.6 + 0.7 + 0.8) / 5
    assert result == pytest.approx(expected, rel=1e-9)


def test_calculate_overall_confidence_empty():
    """Test calculate_overall_confidence with empty inputs."""
    assert calculate_overall_confidence({}) is None
    # Test with empty list (type ignore since function expects dict but handles lists internally)
    assert calculate_overall_confidence([]) is None  # type: ignore[arg-type]

    field_metadata_invalid: Dict[str, Any] = {"invalid": "not_a_number", "also_invalid": None}
    assert calculate_overall_confidence(field_metadata_invalid) is None

    field_metadata_no_confidence: Dict[str, Any] = {
        "field1": ExtractedFieldMetadata(),
        "field2": ExtractedFieldMetadata(),
    }
    assert calculate_overall_confidence(field_metadata_no_confidence) is None


def test_parse_extracted_field_metadata():
    """Test parse_extracted_field_metadata with legacy citation format."""
    raw_metadata: Dict[str, Any] = {
        "name": {
            "confidence": 0.95,
            "citation": [{"page": 1, "matching_text": "John Smith"}],
        },
        "age": {
            "confidence": 0.87,
            "citation": [{"page": 2.0, "matching_text": "25 years old"}],
        },
        "email": {
            "confidence": 0.92,
            "citation": [],
        },
    }

    result = parse_extracted_field_metadata(raw_metadata)
    result2 = parse_extracted_field_metadata(result)
    assert result2 == result

    assert isinstance(result["name"], ExtractedFieldMetadata)
    assert result["name"].confidence == 0.95
    assert result["name"].citation == [FieldCitation(page=1, matching_text="John Smith")]

    assert isinstance(result["age"], ExtractedFieldMetadata)
    assert result["age"].confidence == 0.87
    assert result["age"].citation == [FieldCitation(page=2, matching_text="25 years old")]

    assert isinstance(result["email"], ExtractedFieldMetadata)
    assert result["email"].confidence == 0.92


def test_parse_extracted_field_metadata_complex():
    """Test parse_extracted_field_metadata with new citation format and reasoning field."""
    raw_metadata: Dict[str, Any] = {
        "title": {
            "reasoning": "Combined key parametrics",
            "citation": [{"page": 1, "matching_text": "PHE844/F844"}],
            "extraction_confidence": 0.947,
            "confidence": 0.947,
        },
        "manufacturer": {
            "reasoning": "VERBATIM EXTRACTION",
            "citation": [{"page": 1, "matching_text": "YAGEO KEMET"}],
            "extraction_confidence": 0.999,
            "confidence": 0.999,
        },
        "features": [
            {
                "reasoning": "VERBATIM EXTRACTION",
                "citation": [{"page": 1, "matching_text": "EMI Safety"}],
                "extraction_confidence": 0.999,
                "confidence": 0.999,
            },
        ],
        "dimensions": {
            "length": {
                "citation": [{"page": 1, "matching_text": "L 41mm"}],
                "extraction_confidence": 0.898,
                "confidence": 0.898,
            },
            "reasoning": "VERBATIM EXTRACTION",
        },
    }

    result = parse_extracted_field_metadata(raw_metadata)

    assert isinstance(result["title"], ExtractedFieldMetadata)
    assert result["title"].reasoning == "Combined key parametrics"
    assert result["title"].confidence == 0.947

    assert isinstance(result["manufacturer"], ExtractedFieldMetadata)
    assert result["manufacturer"].reasoning == "VERBATIM EXTRACTION"

    assert isinstance(result["features"], list)
    assert isinstance(result["features"][0], ExtractedFieldMetadata)

    assert isinstance(result["dimensions"], dict)
    assert isinstance(result["dimensions"]["length"], ExtractedFieldMetadata)
    assert result["dimensions"]["length"].reasoning == "VERBATIM EXTRACTION"


def create_file(
    id: str = "file-456",
    name: str = "resume.pdf",
    external_file_id: str = "external-file-id",
    project_id: str = "project-123",
) -> File:
    return model_parse(
        File,
        {
            "id": id,
            "name": name,
            "external_file_id": external_file_id,
            "project_id": project_id,
        },
    )


def create_extract_run(
    id: str = "extract-123",
    job_id: str = "job-123",
    data: Optional[Dict[str, Any]] = None,
    extraction_metadata: Optional[Dict[str, Any]] = None,
    data_schema: Optional[Dict[str, Any]] = None,
    file: Optional[File] = None,
) -> ExtractRun:
    if data is None:
        data = {"name": "John Doe", "age": 30, "email": "john@example.com"}
    if extraction_metadata is None:
        extraction_metadata = {
            "name": {"confidence": 0.95, "citation": [{"page": 1, "matching_text": "John Doe"}]},
            "age": {"confidence": 0.87},
            "email": {"confidence": 0.92, "citation": [{"page": 1, "matching_text": "john@example.com"}]},
        }
    if data_schema is None:
        data_schema = {}
    if file is None:
        file = create_file()

    return model_parse(
        ExtractRun,
        {
            "id": id,
            "job_id": job_id,
            "data": data,
            "extraction_metadata": {"field_metadata": extraction_metadata},
            "data_schema": data_schema,
            "file": file,
            "extraction_agent_id": "extraction-agent-123",
            "config": {},
            "status": "SUCCESS",
            "project_id": str(uuid.uuid4()),
            "from_ui": False,
        },
    )


def test_extracted_data_from_extraction_result_success():
    """Test ExtractedData.from_extraction_result with valid data."""
    extract_run = create_extract_run(
        file=create_file(id="file-456", name="resume.pdf"),
    )

    extracted: ExtractedData[Person] = ExtractedData.from_extraction_result(
        extract_run,
        Person,
        file_hash="abc123",
        status="accepted",
    )

    assert isinstance(extracted.data, Person)
    assert extracted.data.name == "John Doe"
    assert extracted.data.age == 30
    assert extracted.data.email == "john@example.com"
    assert extracted.status == "accepted"
    assert extracted.file_id == "file-456"
    assert extracted.file_name == "resume.pdf"
    assert extracted.file_hash == "abc123"

    assert isinstance(extracted.field_metadata["name"], ExtractedFieldMetadata)
    assert extracted.field_metadata["name"].confidence == 0.95
    assert extracted.field_metadata["name"].citation == [FieldCitation(page=1, matching_text="John Doe")]

    expected_confidence = (0.95 + 0.87 + 0.92) / 3
    assert extracted.overall_confidence == pytest.approx(expected_confidence)


def test_extracted_data_from_extraction_result_with_file_params():
    """Test ExtractedData.from_extraction_result with explicit file parameters."""
    extract_run = create_extract_run(
        file=create_file(id="original-file", name="original.pdf"),
    )

    extracted: ExtractedData[Person] = ExtractedData.from_extraction_result(
        extract_run,
        Person,
        file_id="custom-file-id",
        file_name="custom-name.pdf",
        file_hash="custom-hash",
        metadata={"source": "api_test"},
    )

    assert extracted.file_id == "custom-file-id"
    assert extracted.file_name == "custom-name.pdf"
    assert extracted.file_hash == "custom-hash"
    assert extracted.metadata is not None
    assert extracted.metadata["source"] == "api_test"


def test_extracted_data_from_extraction_result_invalid_data():
    """Test ExtractedData.from_extraction_result with invalid data raises custom exception."""
    extract_run = create_extract_run(
        data={"missing_name": "Valid Name", "age": "not_a_number"},
        extraction_metadata={"name": {"confidence": 0.9}},
        data_schema={},
        file=create_file(id="error-file", name="bad_data.pdf"),
    )

    with pytest.raises(InvalidExtractionData) as exc_info:
        ExtractedData.from_extraction_result(extract_run, Person, metadata={"test": "metadata"})

    invalid_data = exc_info.value.invalid_item
    assert isinstance(invalid_data, ExtractedData)
    assert invalid_data.status == "error"
    assert invalid_data.data == {"missing_name": "Valid Name", "age": "not_a_number"}
    assert invalid_data.file_id == "error-file"
    assert invalid_data.file_name == "bad_data.pdf"

    assert invalid_data.metadata is not None
    assert "extraction_error" in invalid_data.metadata
    assert "test" in invalid_data.metadata
    assert "2 validation errors" in invalid_data.metadata["extraction_error"]


class Dimensions(BaseModel):
    length: Optional[str] = Field(None, description="Length in mm")
    width: Optional[str] = Field(None, description="Width in mm")
    height: Optional[str] = Field(None, description="Height in mm")
    diameter: Optional[str] = Field(None, description="Diameter in mm")
    lead_spacing: Optional[str] = Field(None, description="Lead spacing in mm")


class Capacitor(BaseModel):
    dimensions: Optional[Dimensions] = None


def test_full_parse_nested_dimensions():
    """Test parsing real extraction result with nested dimensions."""
    with open(Path(__file__).parent.parent / "data" / "capacitor.json") as f:
        data = json.load(f)
    result = ExtractedData.from_extraction_result(model_parse(ExtractRun, data), Capacitor)
    expected = {
        "dimensions": {
            "diameter": ExtractedFieldMetadata(
                reasoning="VERBATIM EXTRACTION",
                confidence=1.0,
                extraction_confidence=1.0,
            ),
            "lead_spacing": ExtractedFieldMetadata(
                reasoning="VERBATIM EXTRACTION",
                confidence=0.9999999031936799,
                extraction_confidence=0.9999999031936799,
            ),
            "length": ExtractedFieldMetadata(
                reasoning="VERBATIM EXTRACTION",
                confidence=0.9999968039036192,
                extraction_confidence=0.9999968039036192,
            ),
        }
    }
    assert result.field_metadata == expected
    # Round-trip through JSON to verify serialization/deserialization
    json_str = model_json(result)
    parsed = model_parse(ExtractedData, json.loads(json_str))
    assert parsed.field_metadata == expected


def test_parses_field_metadata_with_error_field():
    """Test that error field in metadata is captured correctly."""
    extract_run = create_extract_run(
        extraction_metadata={
            "name": {"confidence": 0.95, "citation": [{"page": 1, "matching_text": "John Smith"}]},
            "error": "This is an error",
        },
    )

    parsed = ExtractedData.from_extraction_result(extract_run, Person)

    assert parsed.field_metadata == {
        "name": ExtractedFieldMetadata(
            confidence=0.95,
            citation=[FieldCitation(page=1, matching_text="John Smith")],
        ),
    }
    assert parsed.metadata is not None
    assert parsed.metadata.get("field_errors") == "This is an error"
    assert parsed.metadata.get("job_id") == "job-123"


def test_field_conflict_in_schema():
    """Test handling of 'reasoning' field conflict between schema and metadata."""
    raw_metadata: Dict[str, Any] = {
        "majority_opinion": {
            "type": {
                "citation": [{"page": 4, "matching_text": "BARRETT, J."}],
                "parsing_confidence": 1.0,
                "extraction_confidence": 0.999,
                "confidence": 0.999,
            },
            "reasoning": {
                "citation": [{"page": 15, "matching_text": "We hold..."}],
                "parsing_confidence": 1.0,
                "extraction_confidence": 0.414,
                "confidence": 0.414,
            },
        },
        "reasoning": {
            "citation": [{"page": 15, "matching_text": "We hold..."}],
            "parsing_confidence": 1.0,
            "extraction_confidence": 0.414,
            "confidence": 0.414,
        },
    }

    extracted = parse_extracted_field_metadata(raw_metadata)
    assert isinstance(extracted["reasoning"], ExtractedFieldMetadata)
    majority_opinion = extracted["majority_opinion"]
    assert isinstance(majority_opinion, dict)
    assert isinstance(majority_opinion["reasoning"], ExtractedFieldMetadata)


def test_parse_extracted_field_metadata_with_bounding_boxes():
    """Test parse_extracted_field_metadata with bounding boxes and page dimensions."""
    raw_metadata: Dict[str, Any] = {
        "document_type": {
            "citation": [
                {
                    "page": 1,
                    "matching_text": "FACTURE ORIGINALE",
                    "bounding_boxes": [{"x": 77.28, "y": 615.12, "w": 70.6, "h": 7.2}],
                    "page_dimensions": {"width": 222.24, "height": 736.56},
                }
            ],
            "parsing_confidence": 1.0,
            "extraction_confidence": 0.725,
            "confidence": 0.725,
        },
        "summary": {
            "citation": [
                {
                    "page": 1,
                    "matching_text": "FACTURE ORIGINALE",
                    "bounding_boxes": [{"x": 77.28, "y": 615.12, "w": 70.6, "h": 7.2}],
                    "page_dimensions": {"width": 222.24, "height": 736.56},
                },
                {
                    "page": 1,
                    "matching_text": "Cafe filtre - $1.90",
                    "bounding_boxes": [{"x": 10.56, "y": 172.83, "w": 171.85, "h": 497.01}],
                    "page_dimensions": {"width": 222.24, "height": 736.56},
                },
            ],
            "parsing_confidence": 1.0,
            "extraction_confidence": 0.57,
            "confidence": 0.57,
        },
    }

    result = parse_extracted_field_metadata(raw_metadata)

    assert isinstance(result["document_type"], ExtractedFieldMetadata)
    assert result["document_type"].parsing_confidence == 1.0
    assert result["document_type"].extraction_confidence == 0.725
    assert result["document_type"].citation is not None
    assert len(result["document_type"].citation) == 1

    citation = result["document_type"].citation[0]
    assert citation.page == 1
    assert citation.matching_text == "FACTURE ORIGINALE"
    assert citation.bounding_boxes is not None
    assert len(citation.bounding_boxes) == 1
    assert citation.bounding_boxes[0] == BoundingBox(x=77.28, y=615.12, w=70.6, h=7.2)
    assert citation.page_dimensions == PageDimensions(width=222.24, height=736.56)

    assert isinstance(result["summary"], ExtractedFieldMetadata)
    assert result["summary"].citation is not None
    assert len(result["summary"].citation) == 2

    # Verify round-trip serialization
    result2 = parse_extracted_field_metadata(result)
    assert result2 == result
