#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the
web_static folder '''

from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    '''Function to generate a .tgz archive'''
    if not path.exists('versions'):
        local('mkdir versions')
    formater = '%Y%m%d%H%M%S'
    final_file = 'versions/web_static_{}.tgz'\
                 .format(datetime.now().strftime(formater))
    local('tar -czvf {} web_static'.format(final_file))
    return final_file
