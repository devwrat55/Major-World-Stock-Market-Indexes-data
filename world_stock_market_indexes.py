# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:33:08 2020

@author: devwrat
"""

import requests 
from bs4 import BeautifulSoup 
import pandas as pd
prices=[]
names=[]
changes=[]
percentChanges=[]

r= requests.get("https://in.finance.yahoo.com/world-indices")
data=r.text
soup=BeautifulSoup(data, 'html.parser')

for row in soup.find_all('tbody'):
    for srow in row.find_all('tr'):
        for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
        for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
        for change in srow.find_all('td', attrs={'class':'data-col3'}):
            changes.append(change.text)
        for percentChange in srow.find_all('td', attrs={'class':'data-col4'}):
            percentChanges.append(percentChange.text)

df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
df.to_csv('stock_world_indices_data.csv', index = False, header=True)