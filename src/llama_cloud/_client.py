# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    auth,
    evals,
    api_keys,
    projects,
    data_sinks,
    retrievers,
    data_sources,
    validate_integrations,
    embedding_model_configs,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LlamaCloudError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.beta import beta
from .resources.files import files
from .resources.billing import billing
from .resources.parsing import parsing
from .resources.pipelines import pipelines
from .resources.classifier import classifier
from .resources.extraction import extraction
from .resources.organizations import organizations

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LlamaCloud",
    "AsyncLlamaCloud",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.cloud.llamaindex.ai",
    "sandbox": "https://api.staging.llamaindex.ai",
    "staging": "https://api.staging.llamaindex.ai",
}


class LlamaCloud(SyncAPIClient):
    projects: projects.ProjectsResource
    api_keys: api_keys.APIKeysResource
    validate_integrations: validate_integrations.ValidateIntegrationsResource
    data_sinks: data_sinks.DataSinksResource
    data_sources: data_sources.DataSourcesResource
    embedding_model_configs: embedding_model_configs.EmbeddingModelConfigsResource
    organizations: organizations.OrganizationsResource
    files: files.FilesResource
    pipelines: pipelines.PipelinesResource
    retrievers: retrievers.RetrieversResource
    evals: evals.EvalsResource
    parsing: parsing.ParsingResource
    classifier: classifier.ClassifierResource
    auth: auth.AuthResource
    billing: billing.BillingResource
    extraction: extraction.ExtractionResource
    beta: beta.BetaResource
    with_raw_response: LlamaCloudWithRawResponse
    with_streaming_response: LlamaCloudWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "sandbox", "staging"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox", "staging"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LlamaCloud client instance.

        This automatically infers the `api_key` argument from the `LLAMACLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMACLOUD_API_KEY")
        if api_key is None:
            raise LlamaCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LLAMACLOUD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("LLAMA_CLOUD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LLAMA_CLOUD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.projects = projects.ProjectsResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.validate_integrations = validate_integrations.ValidateIntegrationsResource(self)
        self.data_sinks = data_sinks.DataSinksResource(self)
        self.data_sources = data_sources.DataSourcesResource(self)
        self.embedding_model_configs = embedding_model_configs.EmbeddingModelConfigsResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.files = files.FilesResource(self)
        self.pipelines = pipelines.PipelinesResource(self)
        self.retrievers = retrievers.RetrieversResource(self)
        self.evals = evals.EvalsResource(self)
        self.parsing = parsing.ParsingResource(self)
        self.classifier = classifier.ClassifierResource(self)
        self.auth = auth.AuthResource(self)
        self.billing = billing.BillingResource(self)
        self.extraction = extraction.ExtractionResource(self)
        self.beta = beta.BetaResource(self)
        self.with_raw_response = LlamaCloudWithRawResponse(self)
        self.with_streaming_response = LlamaCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLlamaCloud(AsyncAPIClient):
    projects: projects.AsyncProjectsResource
    api_keys: api_keys.AsyncAPIKeysResource
    validate_integrations: validate_integrations.AsyncValidateIntegrationsResource
    data_sinks: data_sinks.AsyncDataSinksResource
    data_sources: data_sources.AsyncDataSourcesResource
    embedding_model_configs: embedding_model_configs.AsyncEmbeddingModelConfigsResource
    organizations: organizations.AsyncOrganizationsResource
    files: files.AsyncFilesResource
    pipelines: pipelines.AsyncPipelinesResource
    retrievers: retrievers.AsyncRetrieversResource
    evals: evals.AsyncEvalsResource
    parsing: parsing.AsyncParsingResource
    classifier: classifier.AsyncClassifierResource
    auth: auth.AsyncAuthResource
    billing: billing.AsyncBillingResource
    extraction: extraction.AsyncExtractionResource
    beta: beta.AsyncBetaResource
    with_raw_response: AsyncLlamaCloudWithRawResponse
    with_streaming_response: AsyncLlamaCloudWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "sandbox", "staging"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox", "staging"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLlamaCloud client instance.

        This automatically infers the `api_key` argument from the `LLAMACLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMACLOUD_API_KEY")
        if api_key is None:
            raise LlamaCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LLAMACLOUD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("LLAMA_CLOUD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LLAMA_CLOUD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.projects = projects.AsyncProjectsResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.validate_integrations = validate_integrations.AsyncValidateIntegrationsResource(self)
        self.data_sinks = data_sinks.AsyncDataSinksResource(self)
        self.data_sources = data_sources.AsyncDataSourcesResource(self)
        self.embedding_model_configs = embedding_model_configs.AsyncEmbeddingModelConfigsResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.pipelines = pipelines.AsyncPipelinesResource(self)
        self.retrievers = retrievers.AsyncRetrieversResource(self)
        self.evals = evals.AsyncEvalsResource(self)
        self.parsing = parsing.AsyncParsingResource(self)
        self.classifier = classifier.AsyncClassifierResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.billing = billing.AsyncBillingResource(self)
        self.extraction = extraction.AsyncExtractionResource(self)
        self.beta = beta.AsyncBetaResource(self)
        self.with_raw_response = AsyncLlamaCloudWithRawResponse(self)
        self.with_streaming_response = AsyncLlamaCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LlamaCloudWithRawResponse:
    def __init__(self, client: LlamaCloud) -> None:
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.validate_integrations = validate_integrations.ValidateIntegrationsResourceWithRawResponse(
            client.validate_integrations
        )
        self.data_sinks = data_sinks.DataSinksResourceWithRawResponse(client.data_sinks)
        self.data_sources = data_sources.DataSourcesResourceWithRawResponse(client.data_sources)
        self.embedding_model_configs = embedding_model_configs.EmbeddingModelConfigsResourceWithRawResponse(
            client.embedding_model_configs
        )
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.pipelines = pipelines.PipelinesResourceWithRawResponse(client.pipelines)
        self.retrievers = retrievers.RetrieversResourceWithRawResponse(client.retrievers)
        self.evals = evals.EvalsResourceWithRawResponse(client.evals)
        self.parsing = parsing.ParsingResourceWithRawResponse(client.parsing)
        self.classifier = classifier.ClassifierResourceWithRawResponse(client.classifier)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.billing = billing.BillingResourceWithRawResponse(client.billing)
        self.extraction = extraction.ExtractionResourceWithRawResponse(client.extraction)
        self.beta = beta.BetaResourceWithRawResponse(client.beta)


class AsyncLlamaCloudWithRawResponse:
    def __init__(self, client: AsyncLlamaCloud) -> None:
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.validate_integrations = validate_integrations.AsyncValidateIntegrationsResourceWithRawResponse(
            client.validate_integrations
        )
        self.data_sinks = data_sinks.AsyncDataSinksResourceWithRawResponse(client.data_sinks)
        self.data_sources = data_sources.AsyncDataSourcesResourceWithRawResponse(client.data_sources)
        self.embedding_model_configs = embedding_model_configs.AsyncEmbeddingModelConfigsResourceWithRawResponse(
            client.embedding_model_configs
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.pipelines = pipelines.AsyncPipelinesResourceWithRawResponse(client.pipelines)
        self.retrievers = retrievers.AsyncRetrieversResourceWithRawResponse(client.retrievers)
        self.evals = evals.AsyncEvalsResourceWithRawResponse(client.evals)
        self.parsing = parsing.AsyncParsingResourceWithRawResponse(client.parsing)
        self.classifier = classifier.AsyncClassifierResourceWithRawResponse(client.classifier)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.billing = billing.AsyncBillingResourceWithRawResponse(client.billing)
        self.extraction = extraction.AsyncExtractionResourceWithRawResponse(client.extraction)
        self.beta = beta.AsyncBetaResourceWithRawResponse(client.beta)


class LlamaCloudWithStreamedResponse:
    def __init__(self, client: LlamaCloud) -> None:
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.validate_integrations = validate_integrations.ValidateIntegrationsResourceWithStreamingResponse(
            client.validate_integrations
        )
        self.data_sinks = data_sinks.DataSinksResourceWithStreamingResponse(client.data_sinks)
        self.data_sources = data_sources.DataSourcesResourceWithStreamingResponse(client.data_sources)
        self.embedding_model_configs = embedding_model_configs.EmbeddingModelConfigsResourceWithStreamingResponse(
            client.embedding_model_configs
        )
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.pipelines = pipelines.PipelinesResourceWithStreamingResponse(client.pipelines)
        self.retrievers = retrievers.RetrieversResourceWithStreamingResponse(client.retrievers)
        self.evals = evals.EvalsResourceWithStreamingResponse(client.evals)
        self.parsing = parsing.ParsingResourceWithStreamingResponse(client.parsing)
        self.classifier = classifier.ClassifierResourceWithStreamingResponse(client.classifier)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.billing = billing.BillingResourceWithStreamingResponse(client.billing)
        self.extraction = extraction.ExtractionResourceWithStreamingResponse(client.extraction)
        self.beta = beta.BetaResourceWithStreamingResponse(client.beta)


class AsyncLlamaCloudWithStreamedResponse:
    def __init__(self, client: AsyncLlamaCloud) -> None:
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.validate_integrations = validate_integrations.AsyncValidateIntegrationsResourceWithStreamingResponse(
            client.validate_integrations
        )
        self.data_sinks = data_sinks.AsyncDataSinksResourceWithStreamingResponse(client.data_sinks)
        self.data_sources = data_sources.AsyncDataSourcesResourceWithStreamingResponse(client.data_sources)
        self.embedding_model_configs = embedding_model_configs.AsyncEmbeddingModelConfigsResourceWithStreamingResponse(
            client.embedding_model_configs
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.pipelines = pipelines.AsyncPipelinesResourceWithStreamingResponse(client.pipelines)
        self.retrievers = retrievers.AsyncRetrieversResourceWithStreamingResponse(client.retrievers)
        self.evals = evals.AsyncEvalsResourceWithStreamingResponse(client.evals)
        self.parsing = parsing.AsyncParsingResourceWithStreamingResponse(client.parsing)
        self.classifier = classifier.AsyncClassifierResourceWithStreamingResponse(client.classifier)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.billing = billing.AsyncBillingResourceWithStreamingResponse(client.billing)
        self.extraction = extraction.AsyncExtractionResourceWithStreamingResponse(client.extraction)
        self.beta = beta.AsyncBetaResourceWithStreamingResponse(client.beta)


Client = LlamaCloud

AsyncClient = AsyncLlamaCloud
