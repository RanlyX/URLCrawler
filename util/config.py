# !usr/bin/python
# -*- coding:utf-8 -*-

import sys
from jsonio import *
from file_check import *

def getConfig(path):
    config=None
    if checkPathExist(path):
        if checkFileExist(path):
            config=readJson(path)
        else:
            print("Configuration file not exist!")
            sys.exit(1)
    else:
            print("Configuration file's Path not found!")
            sys.exit(1)

    return config
