#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to my web servers,
using the function deploy"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.237.112.44', '35.175.63.68']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_pack():
    """Create a compressed archive of your web_static directory"""
    local("mkdir -p versions")
    time_format = "%Y%m%d%H%M%S"
    archive_path = "versions/web_static_{}.tgz".format(
        datetime.utcnow().strftime(time_format))
    command = "tar -cvzf {} web_static".format(archive_path)
    if local(command).succeeded:
        return archive_path

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    file_name = archive_path.split("/")[-1]
    folder_name = file_name.split(".")[0]
    path = "/data/web_static/releases/{}/".format(folder_name)
    run("mkdir -p {}".format(path))
    run("tar -xzf /tmp/{} -C {}".
        format(file_name, path))
    run("rm /tmp/{}".format(file_name))
    run("mv {}web_static/* {}".format(path, path))
    run("rm -rf {}web_static".format(path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(path))
    print("New version deployed!")
    return True

def deploy():
    """Calls the do_pack and do_deploy functions"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
