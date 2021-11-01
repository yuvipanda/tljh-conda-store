"""
Simplest plugin that exercises all the hooks
"""
from tljh.hooks import hookimpl
from pathlib import Path
import subprocess
import os
import sys

@hookimpl
def tljh_extra_apt_packages():
    return [
        'libpq-dev',
    ]



@hookimpl
def tljh_custom_jupyterhub_config(c):
    conda_store_config = Path(__file__).parent / 'conda_store_config.py'
    c.JupyterHub.services = [
        {
            'name': "conda-store",
            'admin': True,
            'url': 'http://localhost:5000',
            'command': [
                '/opt/conda-store/server/bin/conda-store-server',
                '--config', str(conda_store_config)
            ],
            'oauth_redirect_uri': 'http://localhost:12000/services/conda-store/oauth_callback/'
        }
    ]


@hookimpl
def tljh_post_install():
    conda_store_base = Path('/opt/conda-store')
    for d in ['store', 'envs']:
        os.makedirs(conda_store_base / d, exist_ok=True)
    subprocess.check_call([
        '/opt/tljh/user/bin/mamba', 'create', '--prefix', str(conda_store_base / 'server'),
        '-c', 'conda-forge',
        'conda-store-server', '--json', '--yes'
    ])