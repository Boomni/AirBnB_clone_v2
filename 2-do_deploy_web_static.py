#!/usr/bin/python3
""" Deploys archive!
"""
from fabric.api import env, put, run
from os.path import exists
env.hosts = ['54.237.112.44', '35.175.63.68']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ 
    Distributes a .tgz archive from the contents of `web_static/` in AirBnB
    clone repo to the web servers
    Retuns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if not exists(archive_path) or archive_path is None:
        return False

    file_name = archive_path.split('/')[-1]
    dir_name = file_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(dir_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        file_name, dir_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(dir_name) +
        '/data/web_static/releases/{}/'.format(dir_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(dir_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        dir_name))

    print('New version deployed!')
    return True
