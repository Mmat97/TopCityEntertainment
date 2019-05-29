import re
import csv
import sys
import requests
from bs4 import BeautifulSoup




#FUNCTIONS
def csv_generator(csvData):
	with open('output.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
	csvFile.close()

def scraper(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser') 
	if('wikipedia' in url):
		class_value='wikitable sortable'
	elif('previews' in url):
		class_value='articleContents'
	elif('concertarchives' in url):
		class_value='table-responsive'
	return soup.find(class_ = class_value)



def additional_checks(other_cities_list, parsed_text, city_name):
	if(city_name=='New York City'):
		for x in other_cities_list:
			if((x in parsed_text)):
				return x
	return city_name


def hasNum(string_to_check):
	return bool(re.search(r'\d', string_to_check))

def scrape_city_and_states(url,csv,limit):
	cities_and_states=[]
	i=0
	limit_count=0
	for name in scraper(url).find_all('td'):
		z=(name.text).split('[')
		if(not hasNum(z[0])):
			zz=z[0].split('\n')
			if(i==0):
				x=zz[0]
				i=1
			else:
				i=0
				y=zz[0]
				limit_count+=1
				csv.append([str(x.encode('utf-8'))+" "+str(y.encode('utf-8')),0,0,0,0,0,0,0,0,0])
				cities_and_states.append((str(x.encode('utf-8')),str(y.encode('utf-8'))))
				if(limit_count==limit):
					break
		else:
			continue
	return cities_and_states
		



def scrape_stadiums(url,locations,csv,additionals):
	row=0
	for city_state in locations:
		row+=1	
		for stadium_city_state in scraper(url).find_all('tr'):
			#x=stadium_city_state.find(title=re.compile(','))
			stadium_city2=str((stadium_city_state.text).encode('utf-8'))
			#if(x != None):
			#	z=x["title"].split(',')
			#	stadium_city=z[0]
			#else:
			#	stadium_city="n"
			current_state=str(city_state[1])
			current_city=str(additional_checks(additionals,stadium_city2,city_state[0]))
			if((current_city in stadium_city2)):
				y=stadium_city_state
				if(y.has_attr("style")):
					if('Football' in y.text):
						column=csv[0].index('NL_Football')
						csv[row][column]+=1
					elif('Baseball' in y.text): 
						column=csv[0].index('ML_Baseball')
						csv[row][column]+=1
					elif('Soccer' in y.text):
						column=csv[0].index('ML_Soccer')
						csv[row][column]+=1
				else:
					if('Football' in y.text):
						column=csv[0].index('football')
						csv[row][column]+=1
					elif('Baseball' in y.text): 
						column=csv[0].index('baseball')
						csv[row][column]+=1
					elif('Soccer' in y.text):
						column=csv[0].index('soccer')
						csv[row][column]+=1
	#stadium_locations.append((z[0],z[1],))
	return csv


def scrape_comic_or_concerts(url,locations,csv,additionals, find_all_value,column):
	row=0
	if(find_all_value!='location'):
		z=(scraper(url)).find_all(find_all_value)
	else:
		z=(scraper(url)).find_all(href=re.compile(find_all_value))
	for city_state in locations:
		row+=1
		for info in z:
			current_city=additional_checks(additionals,info,city_state[0])
			if(current_city in info.text):	#increment for each city
				csv[row][column]+=1
	return csv









def scrape_other_urls(url,city_and_state_tuples,csv,additionals):
	if('wikipedia' in url):
		return scrape_stadiums(url,city_and_state_tuples,csv,additionals)
	elif('previews' in url):
		return scrape_comic_or_concerts(url,city_and_state_tuples,csv,additionals,'p',csv[0].index('Active Comic-Con'))
	elif('ariana' in url):
		page_count=1
		while(page_count<10):
			urlx=url+str(page_count)
			page5 = requests.get(urlx)
			soup5 = BeautifulSoup(page5.content, 'html.parser')
			ariana_sched = soup5.find(class_ = "table-responsive")
			ariana_sched_page = soup5.find(class_ = "pagination pagination")
			if(str(page_count) not in ariana_sched_page.text):#only 6 pages
				break
			csv=scrape_comic_or_concerts(urlx,city_and_state_tuples,csv,additionals,'location',csv[0].index('Ariana Grande Events'))
			page_count+=1
		return csv
	elif('concertarchives' in url):
		return scrape_comic_or_concerts(url,city_and_state_tuples,csv,additionals,'location',csv[0].index('Dave Chapelle Events'))
	return 






#1. First we initialize the rows of data for each city we obtain
csvData=[['City_State','NL_Football','ML_Baseball','ML_Soccer','football','baseball',
'soccer', 'Active Comic-Con', 'Dave Chapelle Events','Ariana Grande Events']]

#2. We start off the the initial, top cities page from wikipedia
city_url = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'
city_and_state_tuples=scrape_city_and_states(city_url,csvData,5)


#3. Villages/Boroughs within cities 
additionals=['Flushing','Bronx','Brooklyn','Manhattan','Queens','Staten Island', 'New York, NY', 'Garden City']





#4. Compare data from list of cities to other web pages 
entertainment_urls=[]
entertainment_urls.append('https://en.wikipedia.org/wiki/List_of_U.S._stadiums_by_capacity')
entertainment_urls.append('https://www.previewsworld.com/Article/87466-Comic-Convention-Calendar')
entertainment_urls.append('https://www.concertarchives.org/bands/dave-chappelle')
entertainment_urls.append('https://www.concertarchives.org/bands/ariana-grande?page=')



for current_url in entertainment_urls:
	csvData=scrape_other_urls(current_url,city_and_state_tuples,csvData,additionals)

csv_generator(csvData)



