#!/usr/bin/python3
''' Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy'''
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['34.73.122.60', '54.90.72.128']


def do_deploy(archive_path):
    """ Preprares .tgz file to be deployed """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        fname = archive_path.split("/")[-1]
        path_folder = ("/data/web_static/releases/" + fname.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(path_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(fname, path_folder))
        run("sudo rm /tmp/{}".format(fname))
        run("sudo cp -r {}/web_static/* {}/".format(path_folder, path_folder))
        run("sudo rm -rf {}/web_static".format(path_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(path_folder))
        return True
    except Exception:
        return False
