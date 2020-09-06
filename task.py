# !usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

__all__ = ['Task']

# The URL of PhishTank about reported suspicious website.
URL = "https://www.phishtank.com/phish_detail.php?phish_id="
AUTH = "&__cf_chl_captcha_tk__=56d5112d7443999149fc19bc53d4863b06052743-1599304807-0-AezTxSx6i8iQan_CHS1lRxBRrWtgjzWAGlLxo-CmyxIXf6QSHj_Maso356g4M02kycVt8RYwLrX6ZSalf-ecaY5R89eFCEXQr6NAQGB30XB5jxPCVWa2W6RQDn8ztZU0-EMUbn-CHwiztkkFk8XmYk2MzOYRDJa-B6AsrgBiFUTsJZ5etEM7Ku188cbrKohvYzOM3Y16WXakMEsqmAbZ0ES0zKhDSMGZTZZ1k3eeCDZ9cBqPnkS0VOidwKZudPlYAdp9aP7wpGEe__mQwgHVNpdEfmR_NX6NXTaqEOmFKw9t-J-WXvPnPVef60KJyg1r94i2hF0BxQcTdT28vY0UASzyq-VMx2hOseWWlFWOxmO74080EjNtE8hOL0lKwjn5HPrYxJnQX2G9BHv-nXGV97Du0chR1cie0kpOMcEhZu5CVIwXrx0NgQGHFyhMQN9FEfcssrJdIyCOOfDOhatPmt5-jzNm_qRuYgMJapavDcTQTIpwWzDn--RUY1lvmGS3EHIfQy_lI2uhnWjYJXFaIuz0p_rQWBtgWrYJ7gHmQWSfZ21BdAxwyJejJcZhLhDnyuVHZVNshLCUdNZLn8zVkcc"
# To get a webpage content.
def _getPhishDetail(phishID):
    # Force change type to string type
    strPhishID = str(int(phishID))
    
    # Set a useragent
    # ua = UserAgent()
    headers = {
        # Use random will fail.
        # 'User-Agent': ua.random
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'cookies': 'PHPSESSID=2b8t2bg939f47kictnp8k3pto1; __cfduid=df98aa5f888a2772410f480446237e4d71599137918; __utmc=32426495; __utmz=32426495.1599137920.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); cf_clearance=3b6e31cbb74e3480ccb5a658254e91a3c864d6a7-1599288079-0-1z140e6850z2455c598z20280fb6-250; __utma=32426495.1476282257.1599137920.1599145862.1599288083.4',
        # 'Host': "www.phishtank.com",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    # Set a proxy server
    # proxies = {
    #     "http": "http://"+random.choice([
    #         '59.127.164.145:4145',
    #         '210.61.216.66:33990',
    #         '114.24.27.101:80',
    #         '59.124.170.48:60909',
    #         '220.133.209.32:4145',
    #         '118.163.47.38:60909',
    #         '220.132.13.93:4145',
    #         '220.135.2.247:59171',
    #         '114.35.188.117:4145',
    #         '220.134.229.174:4145',
    #         '220.135.50.143:4145',
    #         '220.132.57.245:4145',
    #         '114.32.205.167:4145',
    #         '60.251.40.84:1080',
    #         '118.163.83.21:3128',
    #         '220.130.167.59:60498',
    #         '211.21.92.211:4145',
    #         '123.110.11.185:54845',
    #         '60.251.33.224:80',
    #         '118.163.47.42:60909',
    #         '106.104.151.142:58198',
    #         '60.251.33.225:80',
    #         '118.163.13.200:8080',
    #         '118.167.178.178:8080',
    #         '118.163.47.37:60909',
    #         '118.163.47.39:60909',
    #         '118.163.47.41:60909',
    #         '123.195.152.139:32287',
    #         '59.124.170.47:60909',
    #         '118.163.47.40:60909',
    #         '128.199.244.47:44344',
    #         '128.199.251.160:44344',
    #         '128.199.200.236:44344',
    #         '128.199.193.37:44344',
    #         '128.199.203.84:44344'
    #     ])
    # }

    # Send request to get webpage content
    res = requests.get(URL+strPhishID)
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
    def __init__(self, id_=None, success=False, phish=None):
        self.id_ = id_
        self.success = success
        self.phish = phish

    
    def __str__(self):
        return '{{\n\tid: {0}, \n\tsuccess: {1}, \n\tphish: {2}\n}}'.format(self.id_, self.success, self.phish)
    
    def getPhish(self):
        tempPhish = self.phish
        try:
            webContent = _getPhishDetail(tempPhish.ptid)
            # print(webContent)
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