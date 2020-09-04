# !usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from phish import Phish as Phish
from phish import getPhish as getPhish

def main():
    p = getPhish(1511111)
    print(p)

if __name__ == '__main__':
    main()
