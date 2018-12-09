#!/usr/bin/python
# -*- coding: UTF-8 -*-
# main.py

"SuNing Spider"
__author__ = "Jing Mike"

import requests
import os
import re
import time
import threading
from bs4 import BeautifulSoup


def downloadpage(url):
    '''
    download list page
    '''
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    contents = requests.get(url, headers=headers)
    contents.encoding = 'utf-8'
    return contents.text


def parselist(pagecontents):
    '''
    parse the phone list from the html page
    '''
    result = BeautifulSoup(pagecontents, 'html.parser')
    listpage = result.find_all('li', class_='item-wrap')
    phonelist = []
    for phone in listpage:
        tag = phone.find('div', class_='title-selling-point').find('a')
        phoneurl = tag.get('href')
        phonetitle = tag.get_text()
        phonelist.append(phoneurl)
        break;
    return phonelist


def getphoneinfo(phoneurl):
    phoneurl = 'https:' + phoneurl
    # url = 'https://product.suning.com/0000000000/690128134.html'
    print('URL: ' + phoneurl)
    phonepage = downloadpage(phoneurl)
    soup = BeautifulSoup(phonepage, 'html.parser')
    # seller
    sectionseller = soup.find('div', class_="ds-dianzhao ds-bgnone")
    print('sectionseller')
    print(sectionseller)
    # title
    sectiontitle = soup.find('div', class_="proinfo-title")  # .find_all(['itemDisplayName', 'promotionDesc'])
    print('sectiontitle')
    print(sectiontitle)
    # price
    sectionprice = soup.find('div', class_="proinfo-focus clearfix")  # .find_all(['price-sn', 'price-promo'])
    print('sectionprice')
    print(sectionprice)
    '''
    for i in sectionprice:
        detail = i.find('span', attrs={'class': 'mainprice'}).get_text()
        print(detail)
    '''
    # parameter
    sectionparameter = soup.find('div', class_="tzm")  # .find_all('colorItemList')
    print('sectionparameter')
    print(sectionparameter)


def main():
    # iPhone sold by SuNing.
    url = 'https://search.suning.com/iphone/&ci=20006&hf=brand_Name_FacetAll:Apple&sc=0&ct=1&snyp=&st=0#second-filter'
    listpage = downloadpage(url)
    phonelist = parselist(listpage)
    for phone in phonelist:
        getphoneinfo(phone)


if __name__ == '__main__':
    main()
