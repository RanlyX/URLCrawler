# !usr/bin/python
# -*- coding:utf-8 -*-

import phider.task as mtk
import phider.phish as mp

def main():
    for id_, ptid in enumerate(range(2,3)):
        t = mtk.Task(id_=id_, phish=mp.Phish(ptid)).getPhish()
        print(t)
        # p = t.phish
        # print(p)

if __name__ == '__main__':
    main()
