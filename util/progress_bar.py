# !usr/bin/python
# -*- coding:utf-8 -*-

import sys

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, s):
        '''
        sys.stdout.write(' ' * (self.width*2) + '\r')
        sys.stdout.flush()
        print s
        '''
        progress = self.width * self.count / self.total
        sys.stdout.write(s+' {0:3}/{1:3} ('.format(self.count, self.total))
        sys.stdout.write('%7.3f' % ((float(self.count)/float(self.total))*100))
        sys.stdout.write('%): |')
        sys.stdout.write('#' * progress + ' ' * (self.width - progress) + '|' * 1+"\r")
        if progress == self.width:
            sys.stdout.write('\n')#█
        sys.stdout.flush()
