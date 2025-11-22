# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast
from datetime import datetime

import httpx

from ..types import (
    file_get_params,
    file_delete_params,
    file_upload_params,
    file_read_content_params,
    file_upload_from_url_params,
    file_generate_presigned_url_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.file import File
from .._base_client import make_request_options
from ..types.presigned_url import PresignedURL
from ..types.file_generate_presigned_url_response import FileGeneratePresignedURLResponse

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

    def delete(
        self,
        id: str,
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
        Delete the file from S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/files/{id}",
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

    def generate_presigned_url(
        self,
        *,
        name: str,
        expires_at_seconds: Optional[int] | Omit = omit,
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
    ) -> FileGeneratePresignedURLResponse:
        """
        Create a presigned url for uploading a file.

        The presigned url is valid for a limited time period, after which it will
        expire. Be careful on accidental exposure of the presigned url, as it may allow
        unauthorized access to the file before the expiration.

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
        return self._put(
            "/api/v1/files",
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
                file_generate_presigned_url_params.FileGeneratePresignedURLParams,
            ),
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
                    file_generate_presigned_url_params.FileGeneratePresignedURLParams,
                ),
            ),
            cast_to=FileGeneratePresignedURLResponse,
        )

    def get(
        self,
        id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Read File metadata objects.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}",
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
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=File,
        )

    def read_content(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}/content",
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
                    file_read_content_params.FileReadContentParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    def upload(
        self,
        *,
        upload_file: FileTypes,
        external_file_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a file to S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"upload_file": upload_file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["upload_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/files",
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_file_id": external_file_id,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_upload_params.FileUploadParams,
                ),
            ),
            cast_to=File,
        )

    def upload_from_url(
        self,
        *,
        url: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        follow_redirects: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        proxy_url: Optional[str] | Omit = omit,
        request_headers: Optional[Dict[str, str]] | Omit = omit,
        resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        verify_ssl: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a file to the project from a URL.

        If name is ommitted in the request payload, the file name will be extracted from
        the response Content-Disposition header if available or otherwise it will be
        derived from the URL path.

        If providing the name in the request payload, always suffix the file extension
        in the name if available.

        Args:
          url: URL of the file to download

          follow_redirects: Whether to follow redirects when downloading the file

          name: Name that will be used for created file. If possible, always include the file
              extension in the name.

          proxy_url: URL of the proxy server to use for downloading the file

          request_headers: Headers to include in the request when downloading the file

          resource_info: Resource information for the file

          verify_ssl: Whether to verify the SSL certificate when downloading the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/files/upload_from_url",
            body=maybe_transform(
                {
                    "url": url,
                    "follow_redirects": follow_redirects,
                    "name": name,
                    "proxy_url": proxy_url,
                    "request_headers": request_headers,
                    "resource_info": resource_info,
                    "verify_ssl": verify_ssl,
                },
                file_upload_from_url_params.FileUploadFromURLParams,
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
                    file_upload_from_url_params.FileUploadFromURLParams,
                ),
            ),
            cast_to=File,
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

    async def delete(
        self,
        id: str,
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
        Delete the file from S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/files/{id}",
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

    async def generate_presigned_url(
        self,
        *,
        name: str,
        expires_at_seconds: Optional[int] | Omit = omit,
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
    ) -> FileGeneratePresignedURLResponse:
        """
        Create a presigned url for uploading a file.

        The presigned url is valid for a limited time period, after which it will
        expire. Be careful on accidental exposure of the presigned url, as it may allow
        unauthorized access to the file before the expiration.

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
        return await self._put(
            "/api/v1/files",
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
                file_generate_presigned_url_params.FileGeneratePresignedURLParams,
            ),
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
                    file_generate_presigned_url_params.FileGeneratePresignedURLParams,
                ),
            ),
            cast_to=FileGeneratePresignedURLResponse,
        )

    async def get(
        self,
        id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Read File metadata objects.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}",
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
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=File,
        )

    async def read_content(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}/content",
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
                    file_read_content_params.FileReadContentParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    async def upload(
        self,
        *,
        upload_file: FileTypes,
        external_file_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a file to S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"upload_file": upload_file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["upload_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/files",
            body=await async_maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external_file_id": external_file_id,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_upload_params.FileUploadParams,
                ),
            ),
            cast_to=File,
        )

    async def upload_from_url(
        self,
        *,
        url: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        follow_redirects: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        proxy_url: Optional[str] | Omit = omit,
        request_headers: Optional[Dict[str, str]] | Omit = omit,
        resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        verify_ssl: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a file to the project from a URL.

        If name is ommitted in the request payload, the file name will be extracted from
        the response Content-Disposition header if available or otherwise it will be
        derived from the URL path.

        If providing the name in the request payload, always suffix the file extension
        in the name if available.

        Args:
          url: URL of the file to download

          follow_redirects: Whether to follow redirects when downloading the file

          name: Name that will be used for created file. If possible, always include the file
              extension in the name.

          proxy_url: URL of the proxy server to use for downloading the file

          request_headers: Headers to include in the request when downloading the file

          resource_info: Resource information for the file

          verify_ssl: Whether to verify the SSL certificate when downloading the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/files/upload_from_url",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "follow_redirects": follow_redirects,
                    "name": name,
                    "proxy_url": proxy_url,
                    "request_headers": request_headers,
                    "resource_info": resource_info,
                    "verify_ssl": verify_ssl,
                },
                file_upload_from_url_params.FileUploadFromURLParams,
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
                    file_upload_from_url_params.FileUploadFromURLParams,
                ),
            ),
            cast_to=File,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.generate_presigned_url = to_raw_response_wrapper(
            files.generate_presigned_url,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.read_content = to_raw_response_wrapper(
            files.read_content,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )
        self.upload_from_url = to_raw_response_wrapper(
            files.upload_from_url,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.generate_presigned_url = async_to_raw_response_wrapper(
            files.generate_presigned_url,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.read_content = async_to_raw_response_wrapper(
            files.read_content,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )
        self.upload_from_url = async_to_raw_response_wrapper(
            files.upload_from_url,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.generate_presigned_url = to_streamed_response_wrapper(
            files.generate_presigned_url,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.read_content = to_streamed_response_wrapper(
            files.read_content,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )
        self.upload_from_url = to_streamed_response_wrapper(
            files.upload_from_url,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.generate_presigned_url = async_to_streamed_response_wrapper(
            files.generate_presigned_url,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.read_content = async_to_streamed_response_wrapper(
            files.read_content,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
        self.upload_from_url = async_to_streamed_response_wrapper(
            files.upload_from_url,
        )
