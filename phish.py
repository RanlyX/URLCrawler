class Phish():

    def __init__(self, ptid = None, url = "none", time = "none", state = "none", verify = "none"):
		self.ptid = ptid
		self.url = url
		self.time = time
		self.state = state
		self.verify = verify
    
    def __str__(self):
        return '{{ptid: {0}, url: {1}, time: {2}, state: {3}, verity: {4}}}'.format(self.ptid, self.url, self.time, self.state, self.verify)
