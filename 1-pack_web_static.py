#!/usr/bin/python3
"""Fabric Script"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a compressed archive of the web_static folder."""
    local("mkdir -p versions")

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + now + ".tgz"

    # create the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
