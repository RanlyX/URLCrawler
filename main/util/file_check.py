# !usr/bin/python
# -*- coding:utf-8 -*-
import os

__all__ = ['checkPathExist', 'checkFileExist', 'checkIsLink', 'checkIsDir', 'makeDir']

def checkPathExist(path):
    if os.path.exists(path):
        return True
    else:
        return False

def checkFileExist(filePath):
    if os.path.isfile(filePath):
        return True
    else:
        return False

def checkIsLink(linkPath):
    if os.path.islink(linkPath):
        return True
    else:
        return False

def checkIsDir(dirPath):
    if os.path.isdir(dirPath):
        return True
    else:
        return False

def makeDir(dirPath):
    os.makedirs(dirPath)