#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=filepath
    -i private-key -u user
"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['54.237.112.44', '35.175.63.68']


def do_deploy(archive_path):
    """
    copies archive file from local to my webservers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put('archive_path', '/tmp')
        run(f"mkdir -p /data/web_static/releases/{file_name}")
        run(f"tar -xzvf /tmp/{file_name}.tgz -C /data/web_static/releases/{file_name}/")
        run(f'rm -rf /tmp/{file_name}.tgz')
        run('rm -rf /data/web_static/current')
        run(f'ln -sf /data/web_static/releases/{file_name} /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
