# !usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import division
import signal
import sys
from progressbar import *
from multiprocessing import *
from task import *
from phish import *
import threading
import time

def run(cls_instance, id_, ptid, total):
    return cls_instance.jobs(id_, ptid, total)

def init(pBar):
    global bar
    bar = pBar
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    
class TaskManager():

    def __init__(self, workerNum = 1, start = 1, end = 1, delayLimit = 0.5, delayCounter = 0, punishLimit = 1000):
        self.workerNum = workerNum
        self.start = start
        self.end = end
        self.delayLimit = delayLimit
        self.delayCounter = delayCounter
        self.punishLimit = punishLimit
    
    def __str__(self):
        return '{{\n\tid: {0}, \n\tsuccess: {1}, \n\tphish: {2}\n}}'.format(self.id_, self.success, self.phish)
    
    def doJobs(self):
        ptids = range(self.start, self.end+1)
        total = len(ptids)
        print(total)
        bar = ProgressBar().start()
        # bar.update(int((0 / (total - 1)) * 100))
        # pool = Pool(self.workerNum, initializer=init, initargs=(bar,))
        pool = Pool(self.workerNum)

        
        for id_, ptid in enumerate(ptids):
            pool.apply_async(run, args=(self, id_, ptid, total))
        pool.close()
        pool.join()

        # bar.finish()

    def jobs(self, id_, ptid, total):
        t = Task(id_=id_, phish=Phish(ptid)).getPhish()
        # print(self.delayCounter)
        print(t)
        if self.delayCounter >= self.punishLimit:
            self.delayCounter = 0
            self.delayLimit = self.delayLimit/2
        if t.success:
            self.delayCounter = self.delayCounter+1
        else:
            time.sleep(self.delayLimit)
            t.getPhish()
            self.delayLimit = self.delayLimit*2
            self.delayCounter = 0
            if t.success:
                self.delayCounter = self.delayCounter+1
            else:
                time.sleep(self.delayLimit)
                t.getPhish()
                self.delayLimit = self.delayLimit*2
                self.delayCounter = 0
                print("Request Fail!!")
        print(self.delayLimit, self.delayCounter)
        # print("Delay Limit: %f, Delay Counter: %d" % self.delayLimit, self.delayCounter)
        time.sleep(self.delayLimit)
        
