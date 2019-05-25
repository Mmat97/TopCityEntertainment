import requests
from bs4 import BeautifulSoup

import csv



class Row:
  def __init__(self, cityname, mFootball,mBaseball,mSoccer,football,baseball,soccer):
    self.cityname = cityname
    self.mFootball = mFootball
    self.mBaseball = mBaseball
    self.mSoccer = mSoccer
    self.football = football
    self.baseball = baseball
    self.soccer = soccer
    
  



citylist=[]
citycount=0

url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


url2="https://en.wikipedia.org/wiki/List_of_U.S._stadiums_by_capacity"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')

"""
tb = soup.find("table",{"class":"wikitable sortable"})



for link in tb.find_all('b'):
	print(link.get_text('title'))
    #name = link.find('a')
""" 

tb = soup.find("table", class_ = "wikitable sortable")
tb2 = soup2.find("table", class_ = "wikitable sortable")

for link in tb.find_all('tr'):
	mFcurrent=0
	mBcurrent=0
	mScurrent=0
	Fcurrent=0
	Bcurrent=0
	Scurrent=0
	currentCity=""
	citycount=citycount+1
	if(citycount<7):
		city = link.find('a')
		if (city != None ):
			for link2 in tb2.find_all('tr'):
				currentCity=city.text
				if('Flushing' in link2.text and ('New York' in link2.text)):
					currentCity='Flushing'
				if('Bronx' in link2.text and ('New York' in link2.text)):
					currentCity='Bronx'
				if('Brooklyn' in link2.text and ('New York' in link2.text)):
					currentCity='Brooklyn'
				if('Manhattan' in link2.text and ('New York' in link2.text)):
					currentCity='Manhattan'
				if('Queens' in link2.text and ('New York' in link2.text)):
					currentCity=Queens;
				if('Staten Island' in link2.text and ('New York' in link2.text)):
					currentCity='Staten Island'
				if(currentCity in link2.text):
					if(link2.has_attr("style")):
						if('Football' in link2.text):
							mFcurrent+=1
						elif('Baseball' in link2.text): 
							mBcurrent+=1
						elif('Soccer' in link2.text):
							mScurrent+=1
					else:
						if('Football' in link2.text): 
							Fcurrent+=1
							print(link2)
						elif('Baseball' in link2.text): 
							Bcurrent+=1
						elif('Soccer' in link2.text):
							Scurrent+=1
				else:
					continue
					
					
					
					
					
					
					
        	citylist.append(Row(city.text,mFcurrent,mBcurrent,mScurrent,Fcurrent,Bcurrent,Scurrent))
	else:
		break

       
for x in citylist:
	if (x.cityname!= '[c]' ):
		print("City: " + x.cityname)
		print("MFootball: " ,x.mFootball)
		print("MBaseball: " , x.mBaseball)
		print("MSoccer: " , x.mSoccer)
		print("football: " , x.football)
		print("Baseball: " , x.baseball)
		print("soccer: " , x.soccer)
"""
with open('output.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(citylist)
"""
