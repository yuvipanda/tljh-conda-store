import logging

import os
from conda_store_server.storage import S3Storage
from conda_store_server.server.auth import JupyterHubOAuthAuthentication

# ==================================
#      conda-store settings
# ==================================
c.CondaStore.storage_class = S3Storage
c.CondaStore.store_directory = "/opt/conda-store/conda-store/"
c.CondaStore.environment_directory = "/opt/conda-store/envs/"
c.CondaStore.database_url = "sqlite:////opt/conda-store/db.sqlite"
c.CondaStore.default_uid = 1000
c.CondaStore.default_gid = 100
c.CondaStore.default_permissions = "775"

# ==================================
#        server settings
# ==================================
c.CondaStoreServer.log_level = logging.INFO
c.CondaStoreServer.enable_ui = True
c.CondaStoreServer.enable_api = True
c.CondaStoreServer.enable_registry = True
c.CondaStoreServer.enable_metrics = True
c.CondaStoreServer.address = "0.0.0.0"
c.CondaStoreServer.port = 5000
# This MUST start with `/`
c.CondaStoreServer.url_prefix = os.environ['JUPYTERHUB_SERVICE_PREFIX']


# ==================================
#         auth settings
# ==================================
c.CondaStoreServer.authentication_class = JupyterHubOAuthAuthentication
c.JupyterHubOAuthAuthentication.jupyterhub_url = os.environ['JUPYTERHUB_BASE_URL']
c.JupyterHubOAuthAuthentication.client_id = os.environ['JUPYTERHUB_SERVICE_NAME']
c.JupyterHubOAuthAuthentication.client_secret = os.environ['JUPYTERHUB_API_TOKEN']
c.JupyterHubOAuthAuthentication.authorize_url = f"{os.environ['JUPYTERHUB_BASE_URL']}/hub/api/oauth2/authorize"


# ==================================
#         worker settings
# ==================================
c.CondaStoreWorker.log_level = logging.INFO
c.CondaStoreWorker.watch_paths = ["/opt/conda-store/environments/"]
