 # Webscraping of flipkart site

# pip install requests 
# pip install bs4
# pip install html5lib
import requests
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
Product_name = []
Price= []
Description=[]
Reviews=[]

# for i in range(0,12):
url= 'https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+10000%7CMobiles&requestId=0113cb0c-32f1-4747-8c9b-f55be2f71743&as-searchtext=mobile+under&page=1'
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, 'html.parser' )
box= soup.find('div', class_='_1YokD2 _3Mn1Gg')
# print(soup)
# while True:
np = soup.find('a', class_='_1LKTO3').get("href")
#for getting complete next page link

cnp= 'https://www.flipkart.com'+ np
# print(cnp)
# url = cnp
# r = requests.get(url)
# soup= BeautifulSoup(r.text, "html.parser")
# print( cnp)
# Getting name of the product
names= soup.find_all('div', class_= '_4rR01T')
# print(names)
for i in names:
  name= i.text
Product_name.append(name)
print(Product_name)
# print(len(Product_name))
#for getting price of the product
prices= soup.find_all('div', class_ ='_30jeq3 _1_WHN1')
# print(prices)
for i in prices:
 name = i.text
Price.append(name)
print(Price) 
# print(len(Price)) 
#Getting Description of the product
Desc= soup.find_all('ul', class_='_1xgFaf')
for i in Desc:
 name=i.text
Description.append(name)
print(Description)
#     print(len(Description))

#Getting Reviews of the products.
reviews= box.find_all('div', class_='_3LWZlK')
for i in reviews:
 name=i.text
Reviews.append(name)
print(Reviews)
# print(len(Reviews))
# We get lenth=39 because of extra phones on the webpage here we'll do section scraping
#we will apply div class of perticular section of webpage
df= pd.DataFrame({'Product Name':Product_name,'Prices':Price,'Description':Description,'Reviews':Reviews})
print(df)
