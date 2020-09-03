# !usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

# To get a webpage.
def getPhishState(id):
    url = "https://www.phishtank.com/phish_detail.php?phish_id="
    res = requests.get(url+id)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.h2.text

def main(id):
    if getPhishState(id).find("Submission") > 0:
        print("URL existed.")
    else:
        print("URL not exist.")

if __name__ == '__main__':
    main("0")
    main("15")