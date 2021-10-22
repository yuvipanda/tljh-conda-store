"""
Simplest plugin that exercises all the hooks
"""
from tljh.hooks import hookimpl
from pathlib import Path
import sys

@hookimpl
def tljh_extra_apt_packages():
    return [
        'postgresql',
    ]


@hookimpl
def tljh_config_post_install(config):
    # Put an arbitrary marker we can test for
    config['simplest_plugin'] = {
        'present': True
    }

@hookimpl
def tljh_extra_hub_pip_packages():
    return [
        'psycopg2-binary',
        '/srv/src/conda-store/conda-store-server'
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
                '/opt/tljh/hub/bin/conda-store-server',
                '--config', str(conda_store_config)
            ]
        }
    ]