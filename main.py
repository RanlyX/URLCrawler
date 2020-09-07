# !usr/bin/python
# -*- coding:utf-8 -*-
import sys
from task import *
from phish import *

def main():
    for id_, ptid in enumerate(range(2,3)):
        t = Task(id_=id_, phish=Phish(ptid)).getPhish()
        # print(t)
        p = t.phish
        print(p)

if __name__ == '__main__':
    main()
