# !usr/bin/python
# -*- coding:utf-8 -*-
import sys
from task import *
from phish import *

def main():
    for i in range(1,10001):
        t = Task(id_=i, phish=Phish(i)).getPhish()
        print(t)
        # p = getPhish(i)
        # print(p)

if __name__ == '__main__':
    main()
