# !usr/bin/python
# -*- coding:utf-8 -*-

import util.util as util
import random
import requests
from bs4 import BeautifulSoup

__all__ = ['Task']

# The URL of PhishTank about reported suspicious website.
URL = "https://www.phishtank.com/phish_detail.php?phish_id="
CONFIG_PATH = "config.json"

def _getConfig():
    return util.readJson(CONFIG_PATH)

# To get a webpage content.
def _getPhishDetail(phishID, cookies):
    # Force change type to string type
    strPhishID = str(int(phishID))

    '''
    Set a useragent, can't use now because PhishTank use Cloudflare's
    service that include hCaptcha verification to anti-crawler. Need 
    same user-agent, same cookies, and same C class subnet IP, else
    cloudflare will block.
    '''
    # ua = UserAgent()
    # headers = {
    #     # Use random will fail.
    #     # 'User-Agent': ua.random
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    # }

    # Set a proxy server
    proxyList = _getConfig()['proxies']
    proxies = {
        "http": "http://"+random.choice(proxyList)
    }

    # Send request to get webpage content
    res = requests.get(URL+strPhishID, proxies=proxies)
    print(res.cookies)
    return res.text

# To get the phish web state content.
def _getPhishStateSentence(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.h2.text

# To get state of the phish web.
def _getPhishState(webContent):
    sentence = _getPhishStateSentence(webContent)
    if sentence.lower().find("offline") > 0:
        return "offline"
    elif sentence.lower().find("online") > 0:
        return "online"
    else:
        return "unknown"

# To get reported time of the phish web.
def _getPhishTime(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    timeSentence = soup.select(".small")[0].text
    time = timeSentence[10:timeSentence.find(" by")]
    return time

# To get URL of the phish web.
def _getPhishURL(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.select("span b")[1].text

# To get verify of the phish web.
def _getPhishVerify(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    verifySentence = soup.h3.text
    if verifySentence.find('Is a phish') != -1:
        return 'valid'
    elif verifySentence.find('is not a phishing site') != -1:
        return 'invalid'
    else:
        return 'unknown'

# Check URL webpage if it existed.
def _checkURLExist(webContent):
    if _getPhishStateSentence(webContent).find("Submission") > 0:
        return True
    else:
        return False

class Task():
    def __init__(self, id_=None, success=False, phish=None, cookies=None):
        self.id_ = id_
        self.success = success
        self.phish = phish
        self.cookies = cookies

    
    def __str__(self):
        return '{{\n\tid: {0}, \n\tsuccess: {1}, \n\tphish: {2}\n}}'.format(self.id_, self.success, self.phish)
    
    def getPhish(self):
        tempPhish = self.phish
        try:
            webContent = _getPhishDetail(tempPhish.ptid, self.cookies)
            print(webContent)
        except requests.exceptions.Timeout as e:
            # Maybe set up for a retry, or continue in a retry loop
            # raise SystemExit(e)
            print(e)
            # return tempPhish
        except requests.exceptions.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
            # raise SystemExit(e)
            print(e)
            # return tempPhish
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            # raise SystemExit(e)
            print(e)
            # return tempPhish
        if _checkURLExist(webContent):
            url = _getPhishURL(webContent)
            tempPhish.url = url.encode('utf-8')
            tempPhish.time = _getPhishTime(webContent)
            tempPhish.state = _getPhishState(webContent)
            tempPhish.verify = _getPhishVerify(webContent)
        self.phish = tempPhish
        self.success = True
        return self
    
    