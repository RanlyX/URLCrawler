# !usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import division
 
import sys, time
from progressbar import *
from multiprocessing import *
from task import *
from phish import *
# import util.progress_bar as pb
import threading
import time

def run(cls_instance, id_, ptid, total):
    return cls_instance.jobs(id_, ptid, total)

def init(pBar):
    global bar
    bar = pBar
    
class TaskManager():
    def __init__(self, workerNum = 1, start = 1, end = 1, delayLimit = 0.0625, delayCounter = 0, punishLimit = 1000):
        self.workerNum = workerNum
        self.start = start
        self.end = end
        self.delayLimit = delayLimit
        self.delayCounter = delayCounter
        self.punishLimit = punishLimit
    
    def __str__(self):
        return '{{\n\tid: {0}, \n\tsuccess: {1}, \n\tphish: {2}\n}}'.format(self.id_, self.success, self.phish)
    
    def doJobs(self):
        ptids = range(self.start, self.end)
        total = len(ptids)
        bar = ProgressBar().start()
        bar.update(int((0 / (total - 1)) * 100))
        pool = Pool(self.workerNum, initializer=init, initargs=(bar,))
        
        for id_, ptid in enumerate(ptids):
            pool.apply_async(run, args=(self, id_, ptid, total))
            
        pool.close()
        pool.join()
        bar.finish()

    def jobs(self, id_, ptid, total):
        t = Task(id_=id_, phish=Phish(ptid)).getPhish()
        if self.delayCounter >= 1000:
            self.delayCounter = 0
            self.delayLimit = self.delayLimit/2
        if t.success:
            self.delayCounter = self.delayCounter+1
        else:
            t.getPhish()
            self.delayLimit = self.delayLimit*2
        print(t)
        bar.update(int((id_ / (total - 1)) * 100))
        time.sleep(self.delayLimit)
        
