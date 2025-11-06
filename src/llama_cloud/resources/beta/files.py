# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import file_query_params, file_create_params, file_delete_params
from ...types.file import File
from ..._base_client import make_request_options
from ...types.beta.file_query_response import FileQueryResponse

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
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_source_id: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        file_size: Optional[int] | Omit = omit,
        last_modified_at: Union[str, datetime, None] | Omit = omit,
        permission_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Create a new file in the project.

        Args: file_create: File creation data project: Validated project from dependency
        db: Database session

        Returns: The created file

        Args:
          name: Name that will be used for created file. If possible, always include the file
              extension in the name.

          data_source_id: The ID of the data source that the file belongs to

          external_file_id: The ID of the file in the external system

          file_size: Size of the file in bytes

          last_modified_at: The last modified time of the file

          permission_info: Permission information for the file

          resource_info: Resource information for the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/files",
            body=maybe_transform(
                {
                    "name": name,
                    "data_source_id": data_source_id,
                    "external_file_id": external_file_id,
                    "file_size": file_size,
                    "last_modified_at": last_modified_at,
                    "permission_info": permission_info,
                    "resource_info": resource_info,
                },
                file_create_params.FileCreateParams,
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
                    file_create_params.FileCreateParams,
                ),
            ),
            cast_to=File,
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
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_source_id: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        file_size: Optional[int] | Omit = omit,
        last_modified_at: Union[str, datetime, None] | Omit = omit,
        permission_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Create a new file in the project.

        Args: file_create: File creation data project: Validated project from dependency
        db: Database session

        Returns: The created file

        Args:
          name: Name that will be used for created file. If possible, always include the file
              extension in the name.

          data_source_id: The ID of the data source that the file belongs to

          external_file_id: The ID of the file in the external system

          file_size: Size of the file in bytes

          last_modified_at: The last modified time of the file

          permission_info: Permission information for the file

          resource_info: Resource information for the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/files",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "data_source_id": data_source_id,
                    "external_file_id": external_file_id,
                    "file_size": file_size,
                    "last_modified_at": last_modified_at,
                    "permission_info": permission_info,
                    "resource_info": resource_info,
                },
                file_create_params.FileCreateParams,
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
                    file_create_params.FileCreateParams,
                ),
            ),
            cast_to=File,
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
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.query = to_raw_response_wrapper(
            files.query,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.query = async_to_raw_response_wrapper(
            files.query,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.query = to_streamed_response_wrapper(
            files.query,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.query = async_to_streamed_response_wrapper(
            files.query,
        )
