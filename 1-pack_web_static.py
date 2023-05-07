#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + time + '.tgz'
    local('mkdir -p versions')
    create = local(f'tar -cvzf {archive_path} web_static/')
    if create:
        return archive_path
    return None
