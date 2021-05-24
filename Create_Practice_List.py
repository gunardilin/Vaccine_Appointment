#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /Users/GunardiLin/Desktop/Codes/Vaccine_Appointment/Others/Create_Practice_List.py
# Project: /Users/GunardiLin/Desktop/Codes/Vaccine_Appointment/Others
# Created Date: Monday, May 24th 2021, 3:22:13 pm
# Author: Gunardi Ali
# -----
# Last Modified: Monday, May 24th 2021, 3:38:38 pm
# Modified By: Gunardi Ali
# -----
# Copyright (c) 2021 Gunardi Ali
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

# Get location practice_ids
url1 = 'https://www.doctolib.de/allgemeinmedizin/81667-muenchen'
url2 = 'https://www.doctolib.de/gemeinschaftspraxis/81667-muenchen'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

practice_ids_hrefs_list = []
for url in [url1, url2]:
    for page in range(1, 100):
        payload = {'page':page}

        response = requests.get(url, headers=headers, params=payload)
        if response.status_code == 404:
            print("Page {} was not found".format(page))
            break
        
        else:
            print('Page: %s' %page)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print("Output of response.text: {}".format(response.text))
            divs = soup.find_all('div',{'class':'dl-search-result'})
            
            for count, div in enumerate(divs):
                practice_id = div['id'].split('-')[-1]
                href = soup.find_all('a',{'class':'dl-search-result-name'})[count]['href']
                # practice_href = div['href']
                print(practice_id, href)
                practice_ids_hrefs_list.append(practice_id + ',' + href)
            sleep(1)
with open('practice_list.txt', 'w') as f:
    for item in practice_ids_hrefs_list:
        f.write("%s\n" % item)
# To open href, add: https://doctolib.de/