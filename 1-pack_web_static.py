#!/usr/bin/python3
"""
Fabric script to genereate .tgz archive
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates a folder (versions)
    Creates the archive and compresses it into the versions folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time))
        return ("versions/web_static_{}.tgz".format(time))
    except Exception:
        return None
