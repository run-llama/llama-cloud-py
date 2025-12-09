# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TextNode", "Relationships", "RelationshipsRelatedNodeInfo", "RelationshipsUnionMember1"]


class RelationshipsRelatedNodeInfo(BaseModel):
    node_id: str

    class_name: Optional[str] = None

    hash: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    node_type: Union[Literal["1", "2", "3", "4", "5"], str, None] = None


class RelationshipsUnionMember1(BaseModel):
    node_id: str

    class_name: Optional[str] = None

    hash: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    node_type: Union[Literal["1", "2", "3", "4", "5"], str, None] = None


Relationships: TypeAlias = Union[RelationshipsRelatedNodeInfo, List[RelationshipsUnionMember1]]


class TextNode(BaseModel):
    """Provided for backward compatibility.

    Note: we keep the field with the typo "seperator" to maintain backward compatibility for
    serialized objects.
    """

    class_name: Optional[str] = None

    embedding: Optional[List[float]] = None
    """Embedding of the node."""

    end_char_idx: Optional[int] = None
    """End char index of the node."""

    excluded_embed_metadata_keys: Optional[List[str]] = None
    """Metadata keys that are excluded from text for the embed model."""

    excluded_llm_metadata_keys: Optional[List[str]] = None
    """Metadata keys that are excluded from text for the LLM."""

    extra_info: Optional[Dict[str, object]] = None
    """A flat dictionary of metadata fields"""

    id: Optional[str] = FieldInfo(alias="id_", default=None)
    """Unique ID of the node."""

    metadata_seperator: Optional[str] = None
    """Separator between metadata fields when converting to string."""

    metadata_template: Optional[str] = None
    """Template for how metadata is formatted, with {key} and {value} placeholders."""

    mimetype: Optional[str] = None
    """MIME type of the node content."""

    relationships: Optional[Dict[str, Relationships]] = None
    """A mapping of relationships to other node information."""

    start_char_idx: Optional[int] = None
    """Start char index of the node."""

    text: Optional[str] = None
    """Text content of the node."""

    text_template: Optional[str] = None
    """
    Template for how text is formatted, with {content} and {metadata_str}
    placeholders.
    """
