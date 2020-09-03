# !usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

# To get a webpage.
def getPhishDetail(phishID):
    url = "https://www.phishtank.com/phish_detail.php?phish_id="
    res = requests.get(url+phishID)
    return res.text

def getPhishState(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.h2.text

def getPhishURL(webContent):
    soup = BeautifulSoup(webContent, 'html.parser')
    return soup.select("span b")[1].text

def checkURLExist(webContent):
    if getPhishState(webContent).find("Submission") > 0:
        # print("URL existed.")
        return True
    else:
        # print("URL not exist.")
        return False

def main(phishID):
    try:
        webContent = getPhishDetail(phishID)
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        raise SystemExit(e)
    except requests.exceptions.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        raise SystemExit(e)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
    if checkURLExist(webContent):
        print(getPhishURL(webContent))

if __name__ == '__main__':
    main("0")
    main("15")