# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClassifierRuleParam"]


class ClassifierRuleParam(TypedDict, total=False):
    description: Required[str]
    """Natural language description of what to classify.

    Be specific about the content characteristics that identify this document type.
    """

    type: Required[str]
    """
    The document type to assign when this rule matches (e.g., 'invoice', 'receipt',
    'contract')
    """
