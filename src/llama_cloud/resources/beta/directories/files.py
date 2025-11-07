# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedClassifyJobs, AsyncPaginatedClassifyJobs
from ...._base_client import AsyncPaginator, make_request_options
from ....types.beta.directories import (
    file_add_params,
    file_list_params,
    file_delete_params,
    file_update_params,
    file_retrieve_params,
)
from ....types.beta.directories.file_add_response import FileAddResponse
from ....types.beta.directories.file_list_response import FileListResponse
from ....types.beta.directories.file_update_response import FileUpdateResponse
from ....types.beta.directories.file_retrieve_response import FileRetrieveResponse

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

    def retrieve(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """Get a file by its directory_file_id within the specified directory.

        If you're
        trying to get a file by its unique_id, use the list endpoint with a filter
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return self._get(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=FileRetrieveResponse,
        )

    def update(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        """
        Update file metadata within the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to update a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          display_name: Updated display name.

          unique_id: Updated unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return self._patch(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "unique_id": unique_id,
                },
                file_update_params.FileUpdateParams,
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
                    file_update_params.FileUpdateParams,
                ),
            ),
            cast_to=FileUpdateResponse,
        )

    def list(
        self,
        directory_id: str,
        *,
        display_name: Optional[str] | Omit = omit,
        display_name_contains: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedClassifyJobs[FileListResponse]:
        """
        List all files within the specified directory with optional filtering and
        pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._get_api_list(
            f"/api/v1/beta/directories/{directory_id}/files",
            page=SyncPaginatedClassifyJobs[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "display_name_contains": display_name_contains,
                        "file_id": file_id,
                        "include_deleted": include_deleted,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "unique_id": unique_id,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    def delete(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
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
        Delete a file from the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to delete a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
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

    def add(
        self,
        directory_id: str,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Create a new file within the specified directory.

        The directory must exist and belong to the project passed in. The file_id must
        be provided and exist in the project.

        Args:
          file_id: File ID for the storage location (required).

          display_name: Display name for the file. If not provided, will use the file's name.

          unique_id: Unique identifier for the file in the directory. If not provided, will use the
              file's external_file_id or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._post(
            f"/api/v1/beta/directories/{directory_id}/files",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "display_name": display_name,
                    "unique_id": unique_id,
                },
                file_add_params.FileAddParams,
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
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=FileAddResponse,
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

    async def retrieve(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """Get a file by its directory_file_id within the specified directory.

        If you're
        trying to get a file by its unique_id, use the list endpoint with a filter
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return await self._get(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=FileRetrieveResponse,
        )

    async def update(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        """
        Update file metadata within the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to update a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          display_name: Updated display name.

          unique_id: Updated unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return await self._patch(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "unique_id": unique_id,
                },
                file_update_params.FileUpdateParams,
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
                    file_update_params.FileUpdateParams,
                ),
            ),
            cast_to=FileUpdateResponse,
        )

    def list(
        self,
        directory_id: str,
        *,
        display_name: Optional[str] | Omit = omit,
        display_name_contains: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FileListResponse, AsyncPaginatedClassifyJobs[FileListResponse]]:
        """
        List all files within the specified directory with optional filtering and
        pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._get_api_list(
            f"/api/v1/beta/directories/{directory_id}/files",
            page=AsyncPaginatedClassifyJobs[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "display_name_contains": display_name_contains,
                        "file_id": file_id,
                        "include_deleted": include_deleted,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "unique_id": unique_id,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    async def delete(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
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
        Delete a file from the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to delete a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
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

    async def add(
        self,
        directory_id: str,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Create a new file within the specified directory.

        The directory must exist and belong to the project passed in. The file_id must
        be provided and exist in the project.

        Args:
          file_id: File ID for the storage location (required).

          display_name: Display name for the file. If not provided, will use the file's name.

          unique_id: Unique identifier for the file in the directory. If not provided, will use the
              file's external_file_id or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return await self._post(
            f"/api/v1/beta/directories/{directory_id}/files",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "display_name": display_name,
                    "unique_id": unique_id,
                },
                file_add_params.FileAddParams,
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
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=FileAddResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.update = to_raw_response_wrapper(
            files.update,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.add = to_raw_response_wrapper(
            files.add,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            files.update,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.add = async_to_raw_response_wrapper(
            files.add,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            files.update,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.add = to_streamed_response_wrapper(
            files.add,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            files.update,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            files.add,
        )
