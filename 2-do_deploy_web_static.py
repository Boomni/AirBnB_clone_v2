#!/usr/bin/python3
"""
Fabric script to deploy tgz archive to webservers
"""
from os.path import exists
from fabric.api import env, run, put, local, sudo

env.hosts = ['54.237.112.44', '35.175.63.68']


def do_deploy(archive_path):
    """Copies archive file from local to my webservers"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1].split('.')[0]
        file_folder = '/data/web_static/releases/{file_name}'
        run(f"mkdir -p {file_folder}")
        run(f"tar -xzf /tmp/{file_name}.tgz -C {file_folder}")
        run(f'rm /tmp/{file_name}.tgz')
        run(f'mv {file_folder}/web_static/* {file_folder}')
        run('rm -rf {file_folder}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {file_folder}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
