# !usr/bin/python
# -*- coding:utf-8 -*-

import phider.task as mtk
import phider.phish as mp
import phider.worker as wk
import phider.task_manager as mtm

def main():
    m = mtm.TaskManager(workerNum=10, start=1, end=21)
    m.doJobs()

if __name__ == '__main__':
    main()