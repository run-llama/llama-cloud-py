# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Mapping, Optional, cast

import httpx

from ..types import file_get_params, file_list_params, file_query_params, file_create_params, file_delete_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.presigned_url import PresignedURL
from ..types.file_list_response import FileListResponse
from ..types.file_query_response import FileQueryResponse
from ..types.file_create_response import FileCreateResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        purpose: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """
        Upload a file using multipart/form-data.

        Args:
          file: The file to upload

          purpose: The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract',
              'split', 'classify', 'sheet', 'agent_app'

          external_file_id: The ID of the file in the external system

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
                "external_file_id": external_file_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/beta/files",
            body=maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_create_params.FileCreateParams,
                ),
            ),
            cast_to=FileCreateResponse,
        )

    def list(
        self,
        *,
        external_file_id: Optional[str] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[FileListResponse]:
        """
        List files with optional filtering and pagination.

        This endpoint retrieves files for the specified project with support for
        filtering by various criteria and cursor-based pagination.

        Args:
          external_file_id: Filter by external file ID.

          file_ids: Filter by specific file IDs.

          file_name: Filter by file name (exact match).

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. Defaults to 50, maximum is 1000.

          page_token: A page token received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/files",
            page=SyncPaginatedCursor[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_file_id": external_file_id,
                        "file_ids": file_ids,
                        "file_name": file_name,
                        "order_by": order_by,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single file from the project.

        Args: file_id: The ID of the file to delete project: Validated project from
        dependency db: Database session

        Returns: None (204 No Content on success)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/beta/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        file_id: str,
        *,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Returns a presigned url to read the file content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/api/v1/beta/files/{file_id}/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    @typing_extensions.deprecated("Use the GET /files endpoint instead")
    def query(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        filter: Optional[file_query_params.Filter] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileQueryResponse:
        """
        Query files with flexible filtering and pagination.

        **Deprecated**: Use GET /files instead for listing files with query parameters.

        Args: request: The query request with filters and pagination project: Validated
        project from dependency db: Database session

        Returns: Paginated response with files

        Args:
          filter: Filter parameters for file queries.

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/files/query",
            body=maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                file_query_params.FileQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_query_params.FileQueryParams,
                ),
            ),
            cast_to=FileQueryResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        purpose: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """
        Upload a file using multipart/form-data.

        Args:
          file: The file to upload

          purpose: The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract',
              'split', 'classify', 'sheet', 'agent_app'

          external_file_id: The ID of the file in the external system

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
                "external_file_id": external_file_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/beta/files",
            body=await async_maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_create_params.FileCreateParams,
                ),
            ),
            cast_to=FileCreateResponse,
        )

    def list(
        self,
        *,
        external_file_id: Optional[str] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FileListResponse, AsyncPaginatedCursor[FileListResponse]]:
        """
        List files with optional filtering and pagination.

        This endpoint retrieves files for the specified project with support for
        filtering by various criteria and cursor-based pagination.

        Args:
          external_file_id: Filter by external file ID.

          file_ids: Filter by specific file IDs.

          file_name: Filter by file name (exact match).

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. Defaults to 50, maximum is 1000.

          page_token: A page token received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/files",
            page=AsyncPaginatedCursor[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_file_id": external_file_id,
                        "file_ids": file_ids,
                        "file_name": file_name,
                        "order_by": order_by,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single file from the project.

        Args: file_id: The ID of the file to delete project: Validated project from
        dependency db: Database session

        Returns: None (204 No Content on success)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/beta/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        file_id: str,
        *,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Returns a presigned url to read the file content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/api/v1/beta/files/{file_id}/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    @typing_extensions.deprecated("Use the GET /files endpoint instead")
    async def query(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        filter: Optional[file_query_params.Filter] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileQueryResponse:
        """
        Query files with flexible filtering and pagination.

        **Deprecated**: Use GET /files instead for listing files with query parameters.

        Args: request: The query request with filters and pagination project: Validated
        project from dependency db: Database session

        Returns: Paginated response with files

        Args:
          filter: Filter parameters for file queries.

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/files/query",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                file_query_params.FileQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_query_params.FileQueryParams,
                ),
            ),
            cast_to=FileQueryResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                files.query,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                files.query,  # pyright: ignore[reportDeprecated],
            )
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                files.query,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                files.query,  # pyright: ignore[reportDeprecated],
            )
        )
