# V1

Types:

```python
from llamacloud_prod.types import DeleteParams, V1GetJobsResponse
```

Methods:

- <code title="get /api/v1/jobs">client.v1.<a href="./src/llamacloud_prod/resources/v1/v1.py">get_jobs</a>(\*\*<a href="src/llamacloud_prod/types/v1_get_jobs_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1_get_jobs_response.py">V1GetJobsResponse</a></code>

## Projects

Types:

```python
from llamacloud_prod.types.v1 import (
    AgentDeploymentList,
    Project,
    ProjectCreate,
    ProjectListResponse,
)
```

Methods:

- <code title="post /api/v1/projects">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/project_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project.py">Project</a></code>
- <code title="get /api/v1/projects/{project_id}">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">retrieve</a>(project_id, \*\*<a href="src/llamacloud_prod/types/v1/project_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project.py">Project</a></code>
- <code title="put /api/v1/projects/{project_id}">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">update</a>(project_id, \*\*<a href="src/llamacloud_prod/types/v1/project_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project.py">Project</a></code>
- <code title="get /api/v1/projects">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/project_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/v1/projects/{project_id}">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">delete</a>(project_id, \*\*<a href="src/llamacloud_prod/types/v1/project_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/projects/current">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">get_current</a>(\*\*<a href="src/llamacloud_prod/types/v1/project_get_current_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project.py">Project</a></code>
- <code title="get /api/v1/projects/{project_id}/usage">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">get_usage</a>(project_id, \*\*<a href="src/llamacloud_prod/types/v1/project_get_usage_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/usage_and_plan.py">UsageAndPlan</a></code>
- <code title="get /api/v1/projects/{project_id}/agents">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">list_agents</a>(project_id) -> <a href="./src/llamacloud_prod/types/v1/agent_deployment_list.py">AgentDeploymentList</a></code>
- <code title="post /api/v1/projects/{project_id}/agents:sync">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">sync_agents</a>(project_id) -> <a href="./src/llamacloud_prod/types/v1/agent_deployment_list.py">AgentDeploymentList</a></code>
- <code title="put /api/v1/projects">client.v1.projects.<a href="./src/llamacloud_prod/resources/v1/projects.py">upsert</a>(\*\*<a href="src/llamacloud_prod/types/v1/project_upsert_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/project.py">Project</a></code>

## APIKeys

Types:

```python
from llamacloud_prod.types.v1 import APIKey, APIKeyCreate, APIKeyType, APIKeyListResponse
```

Methods:

- <code title="post /api/v1/api-keys">client.v1.api_keys.<a href="./src/llamacloud_prod/resources/v1/api_keys.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/api_key_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/api_key.py">APIKey</a></code>
- <code title="get /api/v1/api-keys">client.v1.api_keys.<a href="./src/llamacloud_prod/resources/v1/api_keys.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/api_key_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api/v1/api-keys/{api_key_id}">client.v1.api_keys.<a href="./src/llamacloud_prod/resources/v1/api_keys.py">delete</a>(api_key_id) -> None</code>

## ValidateIntegrations

Types:

```python
from llamacloud_prod.types.v1 import (
    AzureOpenAIEmbeddingConfig,
    BaseConnectionValidation,
    BedrockEmbeddingConfig,
    CloudAstraDBVectorStore,
    CloudAzStorageBlobDataSource,
    CloudAzureAISearchVectorStore,
    CloudBoxDataSource,
    CloudConfluenceDataSource,
    CloudJiraDataSource,
    CloudJiraDataSourceV2,
    CloudMilvusVectorStore,
    CloudMongoDBAtlasVectorSearch,
    CloudNotionPageDataSource,
    CloudOneDriveDataSource,
    CloudPineconeVectorStore,
    CloudPostgresVectorStore,
    CloudQdrantVectorStore,
    CloudS3DataSource,
    CloudSharepointDataSource,
    CloudSlackDataSource,
    CohereEmbeddingConfig,
    ConfigurableDataSinkNames,
    ConfigurableDataSourceNames,
    DataSinkCreate,
    DataSourceCreate,
    GeminiEmbeddingConfig,
    HuggingFaceInferenceAPIEmbeddingConfig,
    OpenAIEmbeddingConfig,
    VertexAIEmbeddingConfig,
)
```

Methods:

- <code title="post /api/v1/validate-integrations/validate-data-sink-connection">client.v1.validate_integrations.<a href="./src/llamacloud_prod/resources/v1/validate_integrations.py">validate_data_sink_connection</a>(\*\*<a href="src/llamacloud_prod/types/v1/validate_integration_validate_data_sink_connection_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/base_connection_validation.py">BaseConnectionValidation</a></code>
- <code title="post /api/v1/validate-integrations/validate-data-source-connection">client.v1.validate_integrations.<a href="./src/llamacloud_prod/resources/v1/validate_integrations.py">validate_data_source_connection</a>(\*\*<a href="src/llamacloud_prod/types/v1/validate_integration_validate_data_source_connection_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/base_connection_validation.py">BaseConnectionValidation</a></code>
- <code title="post /api/v1/validate-integrations/validate-embedding-connection">client.v1.validate_integrations.<a href="./src/llamacloud_prod/resources/v1/validate_integrations.py">validate_embedding_connection</a>(\*\*<a href="src/llamacloud_prod/types/v1/validate_integration_validate_embedding_connection_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/base_connection_validation.py">BaseConnectionValidation</a></code>

## DataSinks

Types:

```python
from llamacloud_prod.types.v1 import DataSink, DataSinkListResponse
```

Methods:

- <code title="post /api/v1/data-sinks">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_sink_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_sink.py">DataSink</a></code>
- <code title="get /api/v1/data-sinks/{data_sink_id}">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">retrieve</a>(data_sink_id) -> <a href="./src/llamacloud_prod/types/v1/data_sink.py">DataSink</a></code>
- <code title="put /api/v1/data-sinks/{data_sink_id}">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">update</a>(data_sink_id, \*\*<a href="src/llamacloud_prod/types/v1/data_sink_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_sink.py">DataSink</a></code>
- <code title="get /api/v1/data-sinks">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_sink_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_sink_list_response.py">DataSinkListResponse</a></code>
- <code title="delete /api/v1/data-sinks/{data_sink_id}">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">delete</a>(data_sink_id) -> None</code>
- <code title="put /api/v1/data-sinks">client.v1.data_sinks.<a href="./src/llamacloud_prod/resources/v1/data_sinks.py">upsert</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_sink_upsert_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_sink.py">DataSink</a></code>

## DataSources

Types:

```python
from llamacloud_prod.types.v1 import (
    DataSource,
    DataSourceReaderVersionMetadata,
    DataSourceListResponse,
)
```

Methods:

- <code title="post /api/v1/data-sources">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_source_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_source.py">DataSource</a></code>
- <code title="get /api/v1/data-sources/{data_source_id}">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">retrieve</a>(data_source_id) -> <a href="./src/llamacloud_prod/types/v1/data_source.py">DataSource</a></code>
- <code title="put /api/v1/data-sources/{data_source_id}">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">update</a>(data_source_id, \*\*<a href="src/llamacloud_prod/types/v1/data_source_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_source.py">DataSource</a></code>
- <code title="get /api/v1/data-sources">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_source_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_source_list_response.py">DataSourceListResponse</a></code>
- <code title="delete /api/v1/data-sources/{data_source_id}">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">delete</a>(data_source_id) -> None</code>
- <code title="put /api/v1/data-sources">client.v1.data_sources.<a href="./src/llamacloud_prod/resources/v1/data_sources.py">upsert</a>(\*\*<a href="src/llamacloud_prod/types/v1/data_source_upsert_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/data_source.py">DataSource</a></code>

## EmbeddingModelConfigs

Types:

```python
from llamacloud_prod.types.v1 import (
    EmbeddingModelConfig,
    EmbeddingModelConfigUpdate,
    EmbeddingModelConfigListResponse,
)
```

Methods:

- <code title="post /api/v1/embedding-model-configs">client.v1.embedding_model_configs.<a href="./src/llamacloud_prod/resources/v1/embedding_model_configs.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/embedding_model_config_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/embedding_model_config.py">EmbeddingModelConfig</a></code>
- <code title="put /api/v1/embedding-model-configs/{embedding_model_config_id}">client.v1.embedding_model_configs.<a href="./src/llamacloud_prod/resources/v1/embedding_model_configs.py">update</a>(embedding_model_config_id, \*\*<a href="src/llamacloud_prod/types/v1/embedding_model_config_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/embedding_model_config.py">EmbeddingModelConfig</a></code>
- <code title="get /api/v1/embedding-model-configs">client.v1.embedding_model_configs.<a href="./src/llamacloud_prod/resources/v1/embedding_model_configs.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/embedding_model_config_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/embedding_model_config_list_response.py">EmbeddingModelConfigListResponse</a></code>
- <code title="delete /api/v1/embedding-model-configs/{embedding_model_config_id}">client.v1.embedding_model_configs.<a href="./src/llamacloud_prod/resources/v1/embedding_model_configs.py">delete</a>(embedding_model_config_id, \*\*<a href="src/llamacloud_prod/types/v1/embedding_model_config_delete_params.py">params</a>) -> None</code>
- <code title="put /api/v1/embedding-model-configs">client.v1.embedding_model_configs.<a href="./src/llamacloud_prod/resources/v1/embedding_model_configs.py">upsert</a>(\*\*<a href="src/llamacloud_prod/types/v1/embedding_model_config_upsert_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/embedding_model_config.py">EmbeddingModelConfig</a></code>

## Organizations

Types:

```python
from llamacloud_prod.types.v1 import (
    Organization,
    OrganizationCreate,
    Role,
    UsageAndPlan,
    OrganizationListResponse,
    OrganizationRetrieveRolesResponse,
)
```

Methods:

- <code title="put /api/v1/organizations">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/organization_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organization.py">Organization</a></code>
- <code title="get /api/v1/organizations/{organization_id}">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">retrieve</a>(organization_id) -> <a href="./src/llamacloud_prod/types/v1/organization.py">Organization</a></code>
- <code title="put /api/v1/organizations/{organization_id}">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organization_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organization.py">Organization</a></code>
- <code title="get /api/v1/organizations">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">list</a>() -> <a href="./src/llamacloud_prod/types/v1/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="delete /api/v1/organizations/{organization_id}">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">delete</a>(organization_id) -> None</code>
- <code title="get /api/v1/organizations/{organization_id}/roles">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">retrieve_roles</a>(organization_id) -> <a href="./src/llamacloud_prod/types/v1/organization_retrieve_roles_response.py">OrganizationRetrieveRolesResponse</a></code>
- <code title="get /api/v1/organizations/{organization_id}/usage">client.v1.organizations.<a href="./src/llamacloud_prod/resources/v1/organizations/organizations.py">retrieve_usage</a>(organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organization_retrieve_usage_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/usage_and_plan.py">UsageAndPlan</a></code>

### Default

Methods:

- <code title="put /api/v1/organizations/default">client.v1.organizations.default.<a href="./src/llamacloud_prod/resources/v1/organizations/default.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/organizations/default_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organization.py">Organization</a></code>
- <code title="get /api/v1/organizations/default">client.v1.organizations.default.<a href="./src/llamacloud_prod/resources/v1/organizations/default.py">list</a>() -> <a href="./src/llamacloud_prod/types/v1/organization.py">Organization</a></code>

### Users

Types:

```python
from llamacloud_prod.types.v1.organizations import (
    UserOrganization,
    UserCreateResponse,
    UserListResponse,
)
```

Methods:

- <code title="put /api/v1/organizations/{organization_id}/users">client.v1.organizations.users.<a href="./src/llamacloud_prod/resources/v1/organizations/users/users.py">create</a>(organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/user_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organizations/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /api/v1/organizations/{organization_id}/users">client.v1.organizations.users.<a href="./src/llamacloud_prod/resources/v1/organizations/users/users.py">list</a>(organization_id) -> <a href="./src/llamacloud_prod/types/v1/organizations/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/v1/organizations/{organization_id}/users/{member_user_id}">client.v1.organizations.users.<a href="./src/llamacloud_prod/resources/v1/organizations/users/users.py">delete</a>(member_user_id, \*, organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/user_delete_params.py">params</a>) -> None</code>
- <code title="put /api/v1/organizations/{organization_id}/users/remove">client.v1.organizations.users.<a href="./src/llamacloud_prod/resources/v1/organizations/users/users.py">update_remove</a>(organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/user_update_remove_params.py">params</a>) -> None</code>

#### Roles

Types:

```python
from llamacloud_prod.types.v1.organizations.users import UserOrganizationRole
```

Methods:

- <code title="put /api/v1/organizations/{organization_id}/users/roles">client.v1.organizations.users.roles.<a href="./src/llamacloud_prod/resources/v1/organizations/users/roles.py">create</a>(path_organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/users/role_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organizations/users/user_organization_role.py">UserOrganizationRole</a></code>
- <code title="get /api/v1/organizations/{organization_id}/users/roles">client.v1.organizations.users.roles.<a href="./src/llamacloud_prod/resources/v1/organizations/users/roles.py">list</a>(organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/users/role_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/organizations/users/user_organization_role.py">Optional[UserOrganizationRole]</a></code>

#### Projects

Types:

```python
from llamacloud_prod.types.v1.organizations.users import ProjectListResponse
```

Methods:

- <code title="put /api/v1/organizations/{organization_id}/users/{user_id}/projects">client.v1.organizations.users.projects.<a href="./src/llamacloud_prod/resources/v1/organizations/users/projects.py">create</a>(user_id, \*, organization_id, \*\*<a href="src/llamacloud_prod/types/v1/organizations/users/project_create_params.py">params</a>) -> object</code>
- <code title="get /api/v1/organizations/{organization_id}/users/{user_id}/projects">client.v1.organizations.users.projects.<a href="./src/llamacloud_prod/resources/v1/organizations/users/projects.py">list</a>(user_id, \*, organization_id) -> <a href="./src/llamacloud_prod/types/v1/organizations/users/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/v1/organizations/{organization_id}/users/{user_id}/projects/{project_id}">client.v1.organizations.users.projects.<a href="./src/llamacloud_prod/resources/v1/organizations/users/projects.py">delete</a>(project_id, \*, organization_id, user_id) -> object</code>

## Files

Types:

```python
from llamacloud_prod.types.v1 import (
    File,
    FileCreate,
    PresignedURL,
    FileListResponse,
    FileGeneratePresignedURLResponse,
    FileSyncResponse,
)
```

Methods:

- <code title="get /api/v1/files/{id}">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">retrieve</a>(id, \*\*<a href="src/llamacloud_prod/types/v1/file_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file.py">File</a></code>
- <code title="get /api/v1/files">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/file_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/files/{id}">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">delete</a>(id, \*\*<a href="src/llamacloud_prod/types/v1/file_delete_params.py">params</a>) -> None</code>
- <code title="put /api/v1/files">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">generate_presigned_url</a>(\*\*<a href="src/llamacloud_prod/types/v1/file_generate_presigned_url_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file_generate_presigned_url_response.py">FileGeneratePresignedURLResponse</a></code>
- <code title="get /api/v1/files/{id}/content">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">read_content</a>(id, \*\*<a href="src/llamacloud_prod/types/v1/file_read_content_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>
- <code title="put /api/v1/files/sync">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">sync</a>(\*\*<a href="src/llamacloud_prod/types/v1/file_sync_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file_sync_response.py">FileSyncResponse</a></code>
- <code title="post /api/v1/files">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">upload</a>(\*\*<a href="src/llamacloud_prod/types/v1/file_upload_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file.py">File</a></code>
- <code title="put /api/v1/files/upload_from_url">client.v1.files.<a href="./src/llamacloud_prod/resources/v1/files/files.py">upload_from_url</a>(\*\*<a href="src/llamacloud_prod/types/v1/file_upload_from_url_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file.py">File</a></code>

### PageScreenshots

Types:

```python
from llamacloud_prod.types.v1.files import PageScreenshotMetadata, PageScreenshotListResponse
```

Methods:

- <code title="get /api/v1/files/{id}/page_screenshots/{page_index}">client.v1.files.page_screenshots.<a href="./src/llamacloud_prod/resources/v1/files/page_screenshots.py">retrieve</a>(page_index, \*, id, \*\*<a href="src/llamacloud_prod/types/v1/files/page_screenshot_retrieve_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{id}/page_screenshots">client.v1.files.page_screenshots.<a href="./src/llamacloud_prod/resources/v1/files/page_screenshots.py">list</a>(id, \*\*<a href="src/llamacloud_prod/types/v1/files/page_screenshot_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/files/page_screenshot_list_response.py">PageScreenshotListResponse</a></code>
- <code title="post /api/v1/files/{id}/page_screenshots/{page_index}/presigned_url">client.v1.files.page_screenshots.<a href="./src/llamacloud_prod/resources/v1/files/page_screenshots.py">generate_presigned_url</a>(page_index, \*, id, \*\*<a href="src/llamacloud_prod/types/v1/files/page_screenshot_generate_presigned_url_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>

### PageFigures

Types:

```python
from llamacloud_prod.types.v1.files import PageFigureMetadata, PageFigureListResponse
```

Methods:

- <code title="get /api/v1/files/{id}/page-figures/{page_index}/{figure_name}">client.v1.files.page_figures.<a href="./src/llamacloud_prod/resources/v1/files/page_figures.py">retrieve</a>(figure_name, \*, id, page_index, \*\*<a href="src/llamacloud_prod/types/v1/files/page_figure_retrieve_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{id}/page-figures/{page_index}">client.v1.files.page_figures.<a href="./src/llamacloud_prod/resources/v1/files/page_figures.py">list</a>(page_index, \*, id, \*\*<a href="src/llamacloud_prod/types/v1/files/page_figure_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/files/page_figure_list_response.py">PageFigureListResponse</a></code>
- <code title="post /api/v1/files/{id}/page-figures/{page_index}/{figure_name}/presigned_url">client.v1.files.page_figures.<a href="./src/llamacloud_prod/resources/v1/files/page_figures.py">generate_presigned_url</a>(figure_name, \*, id, page_index, \*\*<a href="src/llamacloud_prod/types/v1/files/page_figure_generate_presigned_url_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>

## Pipelines

Types:

```python
from llamacloud_prod.types.v1 import (
    AdvancedModeTransformConfig,
    AutoTransformConfig,
    LlamaParseParameters,
    LlmParameters,
    ManagedIngestionStatusResponse,
    MessageRole,
    MetadataFilters,
    PageFigureNodeWithScore,
    PageScreenshotNodeWithScore,
    Pipeline,
    PipelineCreate,
    PipelineMetadataConfig,
    PipelineType,
    PresetRetrievalParams,
    RetrievalMode,
    SparseModelConfig,
    PipelineRetrieveResponse,
    PipelineListResponse,
    PipelineRetrieveFiles2Response,
    PipelineRetrievePlaygroundSessionResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/pipeline_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/retrieve">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">retrieve</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipeline_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline_retrieve_response.py">PipelineRetrieveResponse</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">update</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipeline_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>
- <code title="get /api/v1/pipelines">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/pipeline_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline_list_response.py">PipelineListResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">delete</a>(pipeline_id) -> None</code>
- <code title="post /api/v1/pipelines/{pipeline_id}/chat">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">chat</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipeline_chat_params.py">params</a>) -> object</code>
- <code title="post /api/v1/pipelines/{pipeline_id}/copy">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">copy</a>(pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/force-delete">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">force_delete</a>(pipeline_id) -> None</code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files2">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">retrieve_files2</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipeline_retrieve_files2_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline_retrieve_files2_response.py">PipelineRetrieveFiles2Response</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/playground-session">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">retrieve_playground_session</a>(pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipeline_retrieve_playground_session_response.py">PipelineRetrievePlaygroundSessionResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/status">client.v1.pipelines.<a href="./src/llamacloud_prod/resources/v1/pipelines/pipelines.py">retrieve_status</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipeline_retrieve_status_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>

### Sync

Methods:

- <code title="post /api/v1/pipelines/{pipeline_id}/sync">client.v1.pipelines.sync.<a href="./src/llamacloud_prod/resources/v1/pipelines/sync.py">create</a>(pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/sync/cancel">client.v1.pipelines.sync.<a href="./src/llamacloud_prod/resources/v1/pipelines/sync.py">cancel</a>(pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>

### DataSources

Types:

```python
from llamacloud_prod.types.v1.pipelines import (
    PipelineDataSource,
    DataSourceRetrieveDataSourcesResponse,
    DataSourceUpdateDataSourcesResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}">client.v1.pipelines.data_sources.<a href="./src/llamacloud_prod/resources/v1/pipelines/data_sources.py">update</a>(data_source_id, \*, pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/data_source_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/pipeline_data_source.py">PipelineDataSource</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/data-sources">client.v1.pipelines.data_sources.<a href="./src/llamacloud_prod/resources/v1/pipelines/data_sources.py">retrieve_data_sources</a>(pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipelines/data_source_retrieve_data_sources_response.py">DataSourceRetrieveDataSourcesResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status">client.v1.pipelines.data_sources.<a href="./src/llamacloud_prod/resources/v1/pipelines/data_sources.py">retrieve_status</a>(data_source_id, \*, pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync">client.v1.pipelines.data_sources.<a href="./src/llamacloud_prod/resources/v1/pipelines/data_sources.py">sync</a>(data_source_id, \*, pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/data_source_sync_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipeline.py">Pipeline</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}/data-sources">client.v1.pipelines.data_sources.<a href="./src/llamacloud_prod/resources/v1/pipelines/data_sources.py">update_data_sources</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/data_source_update_data_sources_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/data_source_update_data_sources_response.py">DataSourceUpdateDataSourcesResponse</a></code>

### Files

Types:

```python
from llamacloud_prod.types.v1.pipelines import (
    PipelineFile,
    FileCreateResponse,
    FileListResponse,
    FileRetrieveStatusCountsResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/files">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">create</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/file_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/file_create_response.py">FileCreateResponse</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}/files/{file_id}">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">update</a>(file_id, \*, pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/file_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/pipeline_file.py">PipelineFile</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">list</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/file_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/files/{file_id}">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">delete</a>(file_id, \*, pipeline_id) -> None</code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files/{file_id}/status">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">retrieve_status</a>(file_id, \*, pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files/status-counts">client.v1.pipelines.files.<a href="./src/llamacloud_prod/resources/v1/pipelines/files.py">retrieve_status_counts</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/file_retrieve_status_counts_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/file_retrieve_status_counts_response.py">FileRetrieveStatusCountsResponse</a></code>

### Metadata

Types:

```python
from llamacloud_prod.types.v1.pipelines import MetadataCreateResponse
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/metadata">client.v1.pipelines.metadata.<a href="./src/llamacloud_prod/resources/v1/pipelines/metadata.py">create</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/metadata_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/metadata_create_response.py">MetadataCreateResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/metadata">client.v1.pipelines.metadata.<a href="./src/llamacloud_prod/resources/v1/pipelines/metadata.py">delete_all</a>(pipeline_id) -> None</code>

### Documents

Types:

```python
from llamacloud_prod.types.v1.pipelines import (
    CloudDocument,
    CloudDocumentCreate,
    TextNode,
    DocumentCreateResponse,
    DocumentListResponse,
    DocumentRetrieveChunksResponse,
    DocumentRetrievePaginatedResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/documents">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">create</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/document_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">retrieve</a>(document_id, \*, pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipelines/cloud_document.py">CloudDocument</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">list</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/document_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/documents/{document_id}">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">delete</a>(document_id, \*, pipeline_id) -> None</code>
- <code title="post /api/v1/pipelines/{pipeline_id}/documents/force-sync-all">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">force_sync_all</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/document_force_sync_all_params.py">params</a>) -> object</code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">retrieve_chunks</a>(document_id, \*, pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/pipelines/document_retrieve_chunks_response.py">DocumentRetrieveChunksResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/paginated">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">retrieve_paginated</a>(pipeline_id, \*\*<a href="src/llamacloud_prod/types/v1/pipelines/document_retrieve_paginated_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/pipelines/document_retrieve_paginated_response.py">DocumentRetrievePaginatedResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}/status">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">retrieve_status</a>(document_id, \*, pipeline_id) -> <a href="./src/llamacloud_prod/types/v1/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync">client.v1.pipelines.documents.<a href="./src/llamacloud_prod/resources/v1/pipelines/documents.py">sync</a>(document_id, \*, pipeline_id) -> object</code>

## Retrievers

Types:

```python
from llamacloud_prod.types.v1 import (
    CompositeRetrievalMode,
    CompositeRetrievalResult,
    ReRankConfig,
    Retriever,
    RetrieverCreate,
    RetrieverPipeline,
    RetrieverListResponse,
)
```

Methods:

- <code title="post /api/v1/retrievers">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/retriever_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/retriever.py">Retriever</a></code>
- <code title="post /api/v1/retrievers/{retriever_id}/retrieve">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">retrieve</a>(retriever_id, \*\*<a href="src/llamacloud_prod/types/v1/retriever_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/composite_retrieval_result.py">CompositeRetrievalResult</a></code>
- <code title="put /api/v1/retrievers/{retriever_id}">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">update</a>(retriever_id, \*\*<a href="src/llamacloud_prod/types/v1/retriever_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/retriever.py">Retriever</a></code>
- <code title="get /api/v1/retrievers">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/retriever_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/retriever_list_response.py">RetrieverListResponse</a></code>
- <code title="delete /api/v1/retrievers/{retriever_id}">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">delete</a>(retriever_id) -> None</code>
- <code title="post /api/v1/retrievers/retrieve">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">retrieve_direct</a>(\*\*<a href="src/llamacloud_prod/types/v1/retriever_retrieve_direct_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/composite_retrieval_result.py">CompositeRetrievalResult</a></code>
- <code title="put /api/v1/retrievers">client.v1.retrievers.<a href="./src/llamacloud_prod/resources/v1/retrievers.py">upsert</a>(\*\*<a href="src/llamacloud_prod/types/v1/retriever_upsert_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/retriever.py">Retriever</a></code>

## Evals

Types:

```python
from llamacloud_prod.types.v1 import EvalListSupportedModelsResponse
```

Methods:

- <code title="get /api/v1/evals/models">client.v1.evals.<a href="./src/llamacloud_prod/resources/v1/evals.py">list_supported_models</a>() -> <a href="./src/llamacloud_prod/types/v1/eval_list_supported_models_response.py">EvalListSupportedModelsResponse</a></code>

## Parsing

Types:

```python
from llamacloud_prod.types.v1 import (
    FailPageMode,
    LlamaParseSupportedFileExtensions,
    ParserLanguages,
    ParsingHistoryItem,
    ParsingJob,
    ParsingMode,
    StatusEnum,
    ParsingGetParsingHistoryResponse,
    ParsingGetSupportedFileExtensionsResponse,
)
```

Methods:

- <code title="post /api/v1/parsing/screenshot">client.v1.parsing.<a href="./src/llamacloud_prod/resources/v1/parsing/parsing.py">create_screenshot</a>(\*\*<a href="src/llamacloud_prod/types/v1/parsing_create_screenshot_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>
- <code title="get /api/v1/parsing/history">client.v1.parsing.<a href="./src/llamacloud_prod/resources/v1/parsing/parsing.py">get_parsing_history</a>() -> <a href="./src/llamacloud_prod/types/v1/parsing_get_parsing_history_response.py">ParsingGetParsingHistoryResponse</a></code>
- <code title="get /api/v1/parsing/supported_file_extensions">client.v1.parsing.<a href="./src/llamacloud_prod/resources/v1/parsing/parsing.py">get_supported_file_extensions</a>() -> <a href="./src/llamacloud_prod/types/v1/parsing_get_supported_file_extensions_response.py">ParsingGetSupportedFileExtensionsResponse</a></code>
- <code title="post /api/v1/parsing/upload">client.v1.parsing.<a href="./src/llamacloud_prod/resources/v1/parsing/parsing.py">upload_file</a>(\*\*<a href="src/llamacloud_prod/types/v1/parsing_upload_file_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>

### Job

Methods:

- <code title="get /api/v1/parsing/job/{job_id}">client.v1.parsing.job.<a href="./src/llamacloud_prod/resources/v1/parsing/job/job.py">retrieve</a>(job_id) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/read/{filename}">client.v1.parsing.job.<a href="./src/llamacloud_prod/resources/v1/parsing/job/job.py">generate_presigned_url</a>(filename, \*, job_id) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/details">client.v1.parsing.job.<a href="./src/llamacloud_prod/resources/v1/parsing/job/job.py">get_details</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/parameters">client.v1.parsing.job.<a href="./src/llamacloud_prod/resources/v1/parsing/job/job.py">get_parameters</a>(job_id) -> object</code>

#### Result

Types:

```python
from llamacloud_prod.types.v1.parsing.job import (
    ParsingJobJsonResult,
    ParsingJobMarkdownResult,
    ParsingJobStructuredResult,
    ParsingJobTextResult,
)
```

Methods:

- <code title="get /api/v1/parsing/job/{job_id}/result/image/{name}">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_image</a>(name, \*, job_id) -> BinaryAPIResponse</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/json">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_json</a>(job_id, \*\*<a href="src/llamacloud_prod/types/v1/parsing/job/result_get_json_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_json_result.py">ParsingJobJsonResult</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/result/markdown">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_markdown</a>(job_id, \*\*<a href="src/llamacloud_prod/types/v1/parsing/job/result_get_markdown_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_markdown_result.py">ParsingJobMarkdownResult</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/result/pdf">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_pdf</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/structured">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_structured</a>(job_id, \*\*<a href="src/llamacloud_prod/types/v1/parsing/job/result_get_structured_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_structured_result.py">ParsingJobStructuredResult</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/result/text">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_text</a>(job_id, \*\*<a href="src/llamacloud_prod/types/v1/parsing/job/result_get_text_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_text_result.py">ParsingJobTextResult</a></code>
- <code title="get /api/v1/parsing/job/{job_id}/result/xlsx">client.v1.parsing.job.result.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/result.py">get_xlsx</a>(job_id) -> object</code>

##### Raw

Methods:

- <code title="get /api/v1/parsing/job/{job_id}/result/raw/json">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_json</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/raw/markdown">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_markdown</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/raw/pdf">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_pdf</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/raw/structured">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_structured</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/raw/text">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_text</a>(job_id) -> object</code>
- <code title="get /api/v1/parsing/job/{job_id}/result/raw/xlsx">client.v1.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/v1/parsing/job/result/raw.py">get_raw_xlsx</a>(job_id) -> object</code>

## Classifier

### Jobs

Types:

```python
from llamacloud_prod.types.v1.classifier import (
    ClassifierRule,
    ClassifyJob,
    ClassifyParsingConfiguration,
    JobListResponse,
    JobGetResultsResponse,
)
```

Methods:

- <code title="post /api/v1/classifier/jobs">client.v1.classifier.jobs.<a href="./src/llamacloud_prod/resources/v1/classifier/jobs.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/classifier/job_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/classifier/classify_job.py">ClassifyJob</a></code>
- <code title="get /api/v1/classifier/jobs/{classify_job_id}">client.v1.classifier.jobs.<a href="./src/llamacloud_prod/resources/v1/classifier/jobs.py">retrieve</a>(classify_job_id, \*\*<a href="src/llamacloud_prod/types/v1/classifier/job_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/classifier/classify_job.py">ClassifyJob</a></code>
- <code title="get /api/v1/classifier/jobs">client.v1.classifier.jobs.<a href="./src/llamacloud_prod/resources/v1/classifier/jobs.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/classifier/job_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/classifier/job_list_response.py">JobListResponse</a></code>
- <code title="get /api/v1/classifier/jobs/{classify_job_id}/results">client.v1.classifier.jobs.<a href="./src/llamacloud_prod/resources/v1/classifier/jobs.py">get_results</a>(classify_job_id, \*\*<a href="src/llamacloud_prod/types/v1/classifier/job_get_results_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/classifier/job_get_results_response.py">JobGetResultsResponse</a></code>

## Auth

Types:

```python
from llamacloud_prod.types.v1 import AuthReadSelfResponse
```

Methods:

- <code title="get /api/v1/auth/me">client.v1.auth.<a href="./src/llamacloud_prod/resources/v1/auth.py">read_self</a>() -> <a href="./src/llamacloud_prod/types/v1/auth_read_self_response.py">AuthReadSelfResponse</a></code>

## Billing

Types:

```python
from llamacloud_prod.types.v1 import (
    BillingCreateCustomerPortalSessionResponse,
    BillingCreateIntentAndCustomerSessionResponse,
    BillingDowngradePlanResponse,
)
```

Methods:

- <code title="post /api/v1/billing/customer-portal-session">client.v1.billing.<a href="./src/llamacloud_prod/resources/v1/billing/billing.py">create_customer_portal_session</a>(\*\*<a href="src/llamacloud_prod/types/v1/billing_create_customer_portal_session_params.py">params</a>) -> str</code>
- <code title="post /api/v1/billing/create-intent-and-customer-session">client.v1.billing.<a href="./src/llamacloud_prod/resources/v1/billing/billing.py">create_intent_and_customer_session</a>(\*\*<a href="src/llamacloud_prod/types/v1/billing_create_intent_and_customer_session_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/billing_create_intent_and_customer_session_response.py">BillingCreateIntentAndCustomerSessionResponse</a></code>
- <code title="post /api/v1/billing/downgrade-plan">client.v1.billing.<a href="./src/llamacloud_prod/resources/v1/billing/billing.py">downgrade_plan</a>(\*\*<a href="src/llamacloud_prod/types/v1/billing_downgrade_plan_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/billing_downgrade_plan_response.py">BillingDowngradePlanResponse</a></code>

### Metronome

Types:

```python
from llamacloud_prod.types.v1.billing import MetronomeGetDashboardResponse
```

Methods:

- <code title="get /api/v1/billing/metronome/dashboard">client.v1.billing.metronome.<a href="./src/llamacloud_prod/resources/v1/billing/metronome.py">get_dashboard</a>(\*\*<a href="src/llamacloud_prod/types/v1/billing/metronome_get_dashboard_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/billing/metronome_get_dashboard_response.py">MetronomeGetDashboardResponse</a></code>

## Extraction

Methods:

- <code title="post /api/v1/extraction/run">client.v1.extraction.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction.py">run</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction_run_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_job.py">ExtractJob</a></code>

### Jobs

Types:

```python
from llamacloud_prod.types.v1.extraction import (
    ExtractJob,
    WebhookConfiguration,
    JobListResponse,
    JobBatchResponse,
    JobRetrieveResultResponse,
)
```

Methods:

- <code title="post /api/v1/extraction/jobs">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/job_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_job.py">ExtractJob</a></code>
- <code title="get /api/v1/extraction/jobs/{job_id}">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">retrieve</a>(job_id) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_job.py">ExtractJob</a></code>
- <code title="get /api/v1/extraction/jobs">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/job_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/job_list_response.py">JobListResponse</a></code>
- <code title="post /api/v1/extraction/jobs/batch">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">batch</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/job_batch_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/job_batch_response.py">JobBatchResponse</a></code>
- <code title="post /api/v1/extraction/jobs/file">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">file</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/job_file_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_job.py">ExtractJob</a></code>
- <code title="get /api/v1/extraction/jobs/{job_id}/result">client.v1.extraction.jobs.<a href="./src/llamacloud_prod/resources/v1/extraction/jobs.py">retrieve_result</a>(job_id, \*\*<a href="src/llamacloud_prod/types/v1/extraction/job_retrieve_result_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/job_retrieve_result_response.py">JobRetrieveResultResponse</a></code>

### Runs

Types:

```python
from llamacloud_prod.types.v1.extraction import ExtractConfig, ExtractRun, RunListResponse
```

Methods:

- <code title="get /api/v1/extraction/runs/{run_id}">client.v1.extraction.runs.<a href="./src/llamacloud_prod/resources/v1/extraction/runs.py">retrieve</a>(run_id, \*\*<a href="src/llamacloud_prod/types/v1/extraction/run_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_run.py">ExtractRun</a></code>
- <code title="get /api/v1/extraction/runs">client.v1.extraction.runs.<a href="./src/llamacloud_prod/resources/v1/extraction/runs.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/run_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/run_list_response.py">RunListResponse</a></code>
- <code title="delete /api/v1/extraction/runs/{run_id}">client.v1.extraction.runs.<a href="./src/llamacloud_prod/resources/v1/extraction/runs.py">delete</a>(run_id, \*\*<a href="src/llamacloud_prod/types/v1/extraction/run_delete_params.py">params</a>) -> object</code>
- <code title="get /api/v1/extraction/runs/latest-from-ui">client.v1.extraction.runs.<a href="./src/llamacloud_prod/resources/v1/extraction/runs.py">retrieve_latest_from_ui</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/run_retrieve_latest_from_ui_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_run.py">Optional[ExtractRun]</a></code>

### ExtractionAgents

Types:

```python
from llamacloud_prod.types.v1.extraction import (
    ExtractAgent,
    ExtractionAgentRetrieveExtractionAgentsResponse,
)
```

Methods:

- <code title="get /api/v1/extraction/extraction-agents/{extraction_agent_id}">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">retrieve</a>(extraction_agent_id) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_agent.py">ExtractAgent</a></code>
- <code title="put /api/v1/extraction/extraction-agents/{extraction_agent_id}">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">update</a>(extraction_agent_id, \*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agent_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_agent.py">ExtractAgent</a></code>
- <code title="delete /api/v1/extraction/extraction-agents/{extraction_agent_id}">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">delete</a>(extraction_agent_id) -> object</code>
- <code title="post /api/v1/extraction/extraction-agents">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">extraction_agents</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agent_extraction_agents_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_agent.py">ExtractAgent</a></code>
- <code title="get /api/v1/extraction/extraction-agents/default">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">retrieve_default</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agent_retrieve_default_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extract_agent.py">ExtractAgent</a></code>
- <code title="get /api/v1/extraction/extraction-agents">client.v1.extraction.extraction_agents.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/extraction_agents.py">retrieve_extraction_agents</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agent_retrieve_extraction_agents_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extraction_agent_retrieve_extraction_agents_response.py">ExtractionAgentRetrieveExtractionAgentsResponse</a></code>

#### Schema

Types:

```python
from llamacloud_prod.types.v1.extraction.extraction_agents import (
    SchemaGenerateResponse,
    SchemaValidationResponse,
)
```

Methods:

- <code title="post /api/v1/extraction/extraction-agents/schema/generate">client.v1.extraction.extraction_agents.schema.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/schema.py">generate</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agents/schema_generate_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extraction_agents/schema_generate_response.py">SchemaGenerateResponse</a></code>
- <code title="post /api/v1/extraction/extraction-agents/schema/validation">client.v1.extraction.extraction_agents.schema.<a href="./src/llamacloud_prod/resources/v1/extraction/extraction_agents/schema.py">validation</a>(\*\*<a href="src/llamacloud_prod/types/v1/extraction/extraction_agents/schema_validation_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/extraction/extraction_agents/schema_validation_response.py">SchemaValidationResponse</a></code>

## Beta

Types:

```python
from llamacloud_prod.types.v1 import BetaRetrieveQuotaManagementResponse
```

Methods:

- <code title="get /api/v1/beta/quota-management">client.v1.beta.<a href="./src/llamacloud_prod/resources/v1/beta/beta.py">retrieve_quota_management</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta_retrieve_quota_management_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta_retrieve_quota_management_response.py">BetaRetrieveQuotaManagementResponse</a></code>

### APIKeys

Types:

```python
from llamacloud_prod.types.v1.beta import APIKeyRetrieveAPIKeysResponse
```

Methods:

- <code title="get /api/v1/beta/api-keys/{api_key_id}">client.v1.beta.api_keys.<a href="./src/llamacloud_prod/resources/v1/beta/api_keys.py">retrieve</a>(api_key_id) -> <a href="./src/llamacloud_prod/types/v1/api_key.py">APIKey</a></code>
- <code title="delete /api/v1/beta/api-keys/{api_key_id}">client.v1.beta.api_keys.<a href="./src/llamacloud_prod/resources/v1/beta/api_keys.py">delete</a>(api_key_id) -> None</code>
- <code title="post /api/v1/beta/api-keys">client.v1.beta.api_keys.<a href="./src/llamacloud_prod/resources/v1/beta/api_keys.py">api_keys</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/api_key_api_keys_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/api_key.py">APIKey</a></code>
- <code title="get /api/v1/beta/api-keys">client.v1.beta.api_keys.<a href="./src/llamacloud_prod/resources/v1/beta/api_keys.py">retrieve_api_keys</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/api_key_retrieve_api_keys_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/api_key_retrieve_api_keys_response.py">APIKeyRetrieveAPIKeysResponse</a></code>

### Batches

Types:

```python
from llamacloud_prod.types.v1.beta import Batch, BatchRetrieveResponse, BatchListResponse
```

Methods:

- <code title="post /api/v1/beta/batches">client.v1.beta.batches.<a href="./src/llamacloud_prod/resources/v1/beta/batches.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/batch_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/batch.py">Batch</a></code>
- <code title="get /api/v1/beta/batches/{batch_id}">client.v1.beta.batches.<a href="./src/llamacloud_prod/resources/v1/beta/batches.py">retrieve</a>(batch_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/batch_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /api/v1/beta/batches">client.v1.beta.batches.<a href="./src/llamacloud_prod/resources/v1/beta/batches.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/batch_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/batch_list_response.py">BatchListResponse</a></code>

### AgentData

Types:

```python
from llamacloud_prod.types.v1.beta import (
    AgentData,
    AgentDataDeleteResponse,
    AgentDataAggregateResponse,
    AgentDataSearchResponse,
)
```

Methods:

- <code title="get /api/v1/beta/agent-data/{item_id}">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">retrieve</a>(item_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data.py">AgentData</a></code>
- <code title="put /api/v1/beta/agent-data/{item_id}">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">update</a>(item_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data.py">AgentData</a></code>
- <code title="post /api/v1/beta/agent-data/:delete">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">delete</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_delete_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data_delete_response.py">AgentDataDeleteResponse</a></code>
- <code title="post /api/v1/beta/agent-data">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">agent_data</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_agent_data_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data.py">AgentData</a></code>
- <code title="post /api/v1/beta/agent-data/:aggregate">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">aggregate</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_aggregate_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data_aggregate_response.py">AgentDataAggregateResponse</a></code>
- <code title="post /api/v1/beta/agent-data/:search">client.v1.beta.agent_data.<a href="./src/llamacloud_prod/resources/v1/beta/agent_data.py">search</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/agent_data_search_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/agent_data_search_response.py">AgentDataSearchResponse</a></code>

### Files

Types:

```python
from llamacloud_prod.types.v1.beta import FileQueryResponse
```

Methods:

- <code title="put /api/v1/beta/files">client.v1.beta.files.<a href="./src/llamacloud_prod/resources/v1/beta/files.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/file_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/file.py">File</a></code>
- <code title="delete /api/v1/beta/files/{file_id}">client.v1.beta.files.<a href="./src/llamacloud_prod/resources/v1/beta/files.py">delete</a>(file_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/file_delete_params.py">params</a>) -> None</code>
- <code title="post /api/v1/beta/files/query">client.v1.beta.files.<a href="./src/llamacloud_prod/resources/v1/beta/files.py">query</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/file_query_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/file_query_response.py">FileQueryResponse</a></code>

### ParseConfigurations

Types:

```python
from llamacloud_prod.types.v1.beta import (
    ParseConfiguration,
    ParseConfigurationCreate,
    ParseConfigurationQueryResponse,
)
```

Methods:

- <code title="get /api/v1/beta/parse-configurations/{config_id}">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">retrieve</a>(config_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration.py">ParseConfiguration</a></code>
- <code title="put /api/v1/beta/parse-configurations/{config_id}">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">update</a>(config_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_update_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration.py">ParseConfiguration</a></code>
- <code title="delete /api/v1/beta/parse-configurations/{config_id}">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">delete</a>(config_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_delete_params.py">params</a>) -> None</code>
- <code title="post /api/v1/beta/parse-configurations">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">parse_configurations</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_parse_configurations_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration.py">ParseConfiguration</a></code>
- <code title="post /api/v1/beta/parse-configurations/query">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">query</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_query_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration_query_response.py">ParseConfigurationQueryResponse</a></code>
- <code title="get /api/v1/beta/parse-configurations/latest">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">retrieve_latest</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_retrieve_latest_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration.py">Optional[ParseConfiguration]</a></code>
- <code title="get /api/v1/beta/parse-configurations">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">retrieve_parse_configurations</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_retrieve_parse_configurations_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration_query_response.py">ParseConfigurationQueryResponse</a></code>
- <code title="put /api/v1/beta/parse-configurations">client.v1.beta.parse_configurations.<a href="./src/llamacloud_prod/resources/v1/beta/parse_configurations.py">update_parse_configurations</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/parse_configuration_update_parse_configurations_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/parse_configuration.py">ParseConfiguration</a></code>

### Spreadsheet

#### Jobs

Types:

```python
from llamacloud_prod.types.v1.beta.spreadsheet import (
    SpreadsheetJob,
    SpreadsheetParsingConfig,
    JobListResponse,
)
```

Methods:

- <code title="post /api/v1/beta/spreadsheet/jobs">client.v1.beta.spreadsheet.jobs.<a href="./src/llamacloud_prod/resources/v1/beta/spreadsheet/jobs/jobs.py">create</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/spreadsheet/job_create_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/spreadsheet/spreadsheet_job.py">SpreadsheetJob</a></code>
- <code title="get /api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}">client.v1.beta.spreadsheet.jobs.<a href="./src/llamacloud_prod/resources/v1/beta/spreadsheet/jobs/jobs.py">retrieve</a>(spreadsheet_job_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/spreadsheet/job_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/spreadsheet/spreadsheet_job.py">SpreadsheetJob</a></code>
- <code title="get /api/v1/beta/spreadsheet/jobs">client.v1.beta.spreadsheet.jobs.<a href="./src/llamacloud_prod/resources/v1/beta/spreadsheet/jobs/jobs.py">list</a>(\*\*<a href="src/llamacloud_prod/types/v1/beta/spreadsheet/job_list_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/beta/spreadsheet/job_list_response.py">JobListResponse</a></code>

##### Tables

Methods:

- <code title="get /api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}/tables/{table_id}/result/{table_type}">client.v1.beta.spreadsheet.jobs.tables.<a href="./src/llamacloud_prod/resources/v1/beta/spreadsheet/jobs/tables.py">retrieve</a>(table_type, \*, spreadsheet_job_id, table_id, \*\*<a href="src/llamacloud_prod/types/v1/beta/spreadsheet/jobs/table_retrieve_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>

# V2alpha1

## Parse

Methods:

- <code title="post /api/v2alpha1/parse/upload">client.v2alpha1.parse.<a href="./src/llamacloud_prod/resources/v2alpha1/parse.py">upload_file</a>(\*\*<a href="src/llamacloud_prod/types/v2alpha1/parse_upload_file_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>

# Parsing

Types:

```python
from llamacloud_prod.types import (
    ParsingGetParsingHistoryResponse,
    ParsingGetSupportedFileExtensionsResponse,
)
```

Methods:

- <code title="get /api/parsing/history">client.parsing.<a href="./src/llamacloud_prod/resources/parsing/parsing.py">get_parsing_history</a>() -> <a href="./src/llamacloud_prod/types/parsing_get_parsing_history_response.py">ParsingGetParsingHistoryResponse</a></code>
- <code title="get /api/parsing/supported_file_extensions">client.parsing.<a href="./src/llamacloud_prod/resources/parsing/parsing.py">get_supported_file_extensions</a>() -> <a href="./src/llamacloud_prod/types/parsing_get_supported_file_extensions_response.py">ParsingGetSupportedFileExtensionsResponse</a></code>
- <code title="post /api/parsing/screenshot">client.parsing.<a href="./src/llamacloud_prod/resources/parsing/parsing.py">screenshot</a>(\*\*<a href="src/llamacloud_prod/types/parsing_screenshot_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>
- <code title="post /api/parsing/upload">client.parsing.<a href="./src/llamacloud_prod/resources/parsing/parsing.py">upload_file</a>(\*\*<a href="src/llamacloud_prod/types/parsing_upload_file_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>

## Job

Methods:

- <code title="get /api/parsing/job/{job_id}">client.parsing.job.<a href="./src/llamacloud_prod/resources/parsing/job/job.py">retrieve</a>(job_id) -> <a href="./src/llamacloud_prod/types/v1/parsing_job.py">ParsingJob</a></code>
- <code title="get /api/parsing/job/{job_id}/read/{filename}">client.parsing.job.<a href="./src/llamacloud_prod/resources/parsing/job/job.py">generate_presigned_url</a>(filename, \*, job_id) -> <a href="./src/llamacloud_prod/types/v1/presigned_url.py">PresignedURL</a></code>
- <code title="get /api/parsing/job/{job_id}/details">client.parsing.job.<a href="./src/llamacloud_prod/resources/parsing/job/job.py">get_details</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/parameters">client.parsing.job.<a href="./src/llamacloud_prod/resources/parsing/job/job.py">get_parameters</a>(job_id) -> object</code>

### Result

Methods:

- <code title="get /api/parsing/job/{job_id}/result/image/{name}">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_image</a>(name, \*, job_id) -> BinaryAPIResponse</code>
- <code title="get /api/parsing/job/{job_id}/result/json">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_json</a>(job_id, \*\*<a href="src/llamacloud_prod/types/parsing/job/result_get_json_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_json_result.py">ParsingJobJsonResult</a></code>
- <code title="get /api/parsing/job/{job_id}/result/markdown">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_markdown</a>(job_id, \*\*<a href="src/llamacloud_prod/types/parsing/job/result_get_markdown_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_markdown_result.py">ParsingJobMarkdownResult</a></code>
- <code title="get /api/parsing/job/{job_id}/result/pdf">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_pdf</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/structured">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_structured</a>(job_id, \*\*<a href="src/llamacloud_prod/types/parsing/job/result_get_structured_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_structured_result.py">ParsingJobStructuredResult</a></code>
- <code title="get /api/parsing/job/{job_id}/result/text">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_text</a>(job_id, \*\*<a href="src/llamacloud_prod/types/parsing/job/result_get_text_params.py">params</a>) -> <a href="./src/llamacloud_prod/types/v1/parsing/job/parsing_job_text_result.py">ParsingJobTextResult</a></code>
- <code title="get /api/parsing/job/{job_id}/result/xlsx">client.parsing.job.result.<a href="./src/llamacloud_prod/resources/parsing/job/result/result.py">get_xlsx</a>(job_id) -> object</code>

#### Raw

Methods:

- <code title="get /api/parsing/job/{job_id}/result/raw/json">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_json</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/raw/markdown">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_markdown</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/raw/pdf">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_pdf</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/raw/structured">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_structured</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/raw/text">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_text</a>(job_id) -> object</code>
- <code title="get /api/parsing/job/{job_id}/result/raw/xlsx">client.parsing.job.result.raw.<a href="./src/llamacloud_prod/resources/parsing/job/result/raw.py">get_xlsx</a>(job_id) -> object</code>
