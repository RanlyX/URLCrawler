# !usr/bin/python
# -*- coding:utf-8 -*-
import requests

# To get a webpage.
def main():
    url = "https://www.phishtank.com/phish_detail.php?phish_id="
    res = requests.get(url+"15")
    return res.text

if __name__ == '__main__':
    print(main())