# !usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

__all__ = ['getPhish', 'Phish']

URL = "https://www.phishtank.com/phish_detail.php?phish_id="

# To get a webpage content.
def _getPhishDetail(phishID):
    if type(phishID) == type(1):
        strPhishID = str(phishID)
    else:
        strPhishID = phishID
    res = requests.get(URL+strPhishID)
    return res.text

# To get the phish web state content.
def _getPhishStateSentence(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.h2.text

# To get state of the phish web .
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
    # return soup.find_all("span", class_="small").span.text
    timeSentence = soup.select(".small")[0].text
    time = timeSentence[:timeSentence.find(" by")]
    return time

# To get URL of the phish web.
def _getPhishURL(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.select("span b")[1].text

def _getPhishVerify(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    verifySentence = soup.h3.text
    if verifySentence.find('Is a phish') != -1:
        return 'valid'
    elif verifySentence.find('is not a phishing site') != -1:
        return 'invalid'
    else:
        return 'unknown'

def _checkURLExist(webContent):
    if _getPhishStateSentence(webContent).find("Submission") > 0:
        # print("URL existed.")
        return True
    else:
        # print("URL not exist.")
        return False

def getPhish(phishID):
    tempPhish = Phish(phishID)
    try:
        webContent = _getPhishDetail(phishID)
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        raise SystemExit(e)
    except requests.exceptions.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        raise SystemExit(e)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
    if _checkURLExist(webContent):
        # print(getPhishURL(webContent))
        tempPhish.url = _getPhishURL(webContent)
        tempPhish.time = _getPhishTime(webContent)
        tempPhish.state = _getPhishState(webContent)
        tempPhish.verify = _getPhishVerify(webContent)
    return tempPhish

class Phish():
    def __init__(self, ptid = None, url = "none", time = "none", state = "none", verify = "none"):
        self.ptid = ptid
        self.url = url
        self.time = time
        self.state = state
        self.verify = verify
    
    def __str__(self):
        return '{{ptid: {0}, url: {1}, time: {2}, state: {3}, verity: {4}}}'.format(self.ptid, self.url, self.time, self.state, self.verify)
