# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .llama_parse_supported_file_extensions import LlamaParseSupportedFileExtensions

__all__ = ["ParsingGetSupportedFileExtensionsResponse"]

ParsingGetSupportedFileExtensionsResponse: TypeAlias = List[LlamaParseSupportedFileExtensions]
