import requests
import pandas as pd
from bs4 import BeautifulSoup
url= 'https://www.iplt20.com/auction/2022'
r=requests.get(url)
# print(r)
soup= BeautifulSoup(r.text,'html.parser')
# print(soup)

table= soup.find('table', class_ = 'ih-td-tab auction-tbl')
title= table.find_all('th')
# print(title)
header= []
for i in title:
     name= i.text
     header.append(name)
    #  print(header)
df = pd.DataFrame(columns= header)
# print(table)
# print(df)
rows= table.find_all('tr')
# print(rows)
for i in rows[1:]:
     first_td= i.find_all('td')[0].find('div', class_="ih-pt-ic").text.strip()
     Data= i.find_all('td')[1:]
     row= [tr.text for tr in Data]
     row.insert(0,first_td)
     l= len(df)
     df.loc[l]= row
     print(df)
     df.to_csv('IPL Auction Statistics.csv')


