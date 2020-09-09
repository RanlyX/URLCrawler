# !usr/bin/python
# -*- coding:utf-8 -*-

import json

# Writing JSON data
def writeJson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

# Reading data back
def readJson(path):
    with open(path, 'r') as f:
        data = json.load(f)
        return data