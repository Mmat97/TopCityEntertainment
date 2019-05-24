import requests
from bs4 import BeautifulSoup

import csv

citylist=[]
citycount=0
url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""
tb = soup.find("table",{"class":"wikitable sortable"})



for link in tb.find_all('b'):
	print(link.get_text('title'))
    #name = link.find('a')
""" 

tb = soup.find("table", class_ = "wikitable sortable")

for link in tb.find_all('tr'):
    #link_row = link.find('td')
    citycount=citycount+1
    if(citycount<7):
    	city = link.find('a')
    	if city != None and city.text != '[c]':
        	link_name = city.text
        	citylist.append(link_name)
    else:
    	break
       
print(citylist)
