#!/usr/bin/python3
"""
Distributes achives to my web browser
"""
import os
from fabric.api import env, put, run

env.hosts = ['54.237.112.44', '35.175.63.68']


def do_deploy(archive_path):
    """
    Deploys the archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory of web server
        put(archive_path, "/tmp/")

        # Get filename without extension
        filename = os.path.basename(archive_path).split(".")[0]

        # Create directory for new version
        run("mkdir -p /data/web_static/releases/{}/".format(filename))

        # Uncompress archive into new directory
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(filename, filename))

        # Delete archive from web server
        run("rm /tmp/{}.tgz".format(filename))

        # Move files out of subdirectory
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(filename, filename))

        # Remove empty directory
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename))

        # Remove symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(filename))

        return True

    except:
        return False
