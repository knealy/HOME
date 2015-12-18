#!/usr/bin/env python

# Kyle Nealy
# Knealy@indiana.edu
# 2/17/15
# C343: a5.py

import httplib2
from bs4 import BeautifulSoup
from random import *



# Pageranking:

def collect_statistics (www,prob,k) :
    result = dict()
    current = choice(www.keys())
    while k >= 0 :
        if current in result.keys():
            result[current] += 1
        else:
            result[current] = 0
        if random() * 100 < prob :
            current = choice(www.keys())
        else :
            neighbors = www[current]
            current = choice(neighbors)
        k -=1
    return result

def top (www) :
    d = collect_statistics(www,15,1000000)
    d = d.items()
    d.sort(key = lambda x : x[1], reverse = True)
    return d[:3]



# PageCrawling:

def get_links(www):
    result = []
    http = httplib2.Http()
    status, response = http.request(www)
    soup = BeautifulSoup(response)
    links = soup.find_all('a')
    for i in range(len(links)):
        url = links[i].get('href')
        result.append(url)
    return result

def update_graph(start_page, www):
    page_links = get_links(start_page)
    www[start_page] = page_links  
    return interweb        

def build_graph(start_page, www):
    if get_links(start_page):
        www = update_graph(start_page,www)
        for i in range(len(get_links(start_page))):
            next_page = www[start_page][i]
            www = update_graph(next_page, www)
    return www
   
