#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *

def do_pack():
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time))
        return ("versions/web_static_{}.tgz".format(time))
    except:
        return None
