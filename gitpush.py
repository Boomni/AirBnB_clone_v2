from fabric.api import *
def push(msg="Update"):
    local(f"git add .; git commit -m '{msg}'")
