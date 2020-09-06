# !usr/bin/python
# -*- coding:utf-8 -*-

class Phish():
    def __init__(self, ptid = None, url = "none", time = "none", state = "none", verify = "none"):
        self.ptid = ptid
        self.url = url
        self.time = time
        self.state = state
        self.verify = verify
    
    def __str__(self):
        return '{{\n\tptid: {0}, \n\turl: {1}, \n\ttime: {2}, \n\tstate: {3}, \n\tverity: {4}\n}}'.format(self.ptid, self.url, self.time, self.state, self.verify)
