# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:58:08 2024

@author: dragon
"""

import requests
from bs4 import BeautifulSoup
import autoMad
import wordGrabber


def getPage(url):
    response = requests.get(url)
    html_data = response.text
    soup = BeautifulSoup(html_data,"html.parser")
    return soup

def madPage(url, sillyFactor):
    soup=getPage(url)
    dictionary = wordGrabber.getDictionary()
    #text = soup.body.find_all(string=True)
    for line in soup.body.find_all(string=True):
        line.replace_with(autoMad.autoMad(line,sillyFactor,dictionary))
    stringSoup = str(soup)
    return stringSoup
    
