#!/usr/bin/python
# -*- coding:utf-8 -*-

import re

def removeSpaceLike(string)：
    return re.sub(r"\s", "", string)

def removeNewLine(string)：
    return re.sub(r"\n", "", string)

def removeSpace(string)：
    return re.sub(r" ", "", string)

def removeTab(string)：
    return re.sub(r"\t", "", string)

def removeSpaceLike(string)：
    return re.sub(r"　", "", string)

def removeCarriage(string)：
    return re.sub(r"\r", "", string)

def getUTF8(s):
    charset = chardet.detect(bytes(s))
    s = s.decode(charset['encoding'], 'ignore').encode('utf-8')
    return s