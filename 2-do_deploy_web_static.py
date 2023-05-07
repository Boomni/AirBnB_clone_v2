#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=filepath
    -i private-key -u user
"""

from os.path import exists
from fabric.api import run, put, local, sudo

env.hosts = ['54.237.112.44', '35.175.63.68']


def do_deploy(archive_path):
    """
    copies archive file from local to my webservers
    """

    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1].split('.')[0]
        run(f"mkdir -p /data/web_static/releases/{file_name}")
        run(f"tar -xzf /tmp/{file_name}.tgz -C /data/web_static/releases/{file_name}/")
        run(f'rm /tmp/{file_name}.tgz')
        run(f'mv /data/web_static/releases/{file_name}/web_static/* /data/web_static/releases/{file_name}')
        run('rm -rf /data/web_static/releases/{file_name}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{file_name}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
