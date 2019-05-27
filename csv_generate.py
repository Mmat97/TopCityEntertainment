import csv
import requests
from bs4 import BeautifulSoup
import sys
import re
  
#Retrieve Data and parse in to html for each web page specified
url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 
city_table = soup.find("table", class_ = "wikitable sortable")

url2="https://en.wikipedia.org/wiki/List_of_U.S._stadiums_by_capacity"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')
stadium_table = soup2.find("table", class_ = "wikitable sortable")

url3="https://www.previewsworld.com/Article/87466-Comic-Convention-Calendar"
page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.content, 'html.parser')
comic_sched = soup3.find(class_ = "articleContents")

url4="https://www.concertarchives.org/bands/dave-chappelle"
page4 = requests.get(url4)
soup4 = BeautifulSoup(page4.content, 'html.parser')
dave_sched = soup4.find(class_ = "table-responsive")

#Initialize csv with columns 
	#NL_Football=NFL owned stadium built
	#ML_Baseball=MLB owned stadium built
	#ML_Soccer=MLS owned stadium built
csvData=[['City', 'State','NL_Football','ML_Baseball','ML_Soccer','football','baseball',
'soccer', 'Active Comic-Con', 'Dave Chapelle Events']]








def csv_generator(csvData):
	with open('output.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
	csvFile.close()

def additional_checks(other_cities_list, parsed_text, city_name,current_state):
	if(city_name=='New York City'):
		for x in other_cities_list:
			if((x in parsed_text) and (current_state in parsed_text)):
				return x
	return city_name

#if state is not given 
def additional_checks2(other_cities_list, parsed_text, city_name):
	if(city_name=='New York City'):
		for x in other_cities_list:
			if((x in parsed_text)):
				return x
	return city_name

def missing_data_exception(x):
	if(x==None):
		print("Missing web data")
		sys.exit(1)



def scanner_one(sched,list_of_cities,num,list_to_check, find_all_value):
	missing_data_exception(sched)
	count=0
	for y in list_of_cities:
		count+=1
		if(find_all_value!='location'):
			for info in sched.find_all(find_all_value):
				current_city=additional_checks2(list_to_check,info.text,y)
				if(current_city in info.text):	#increment for each city
					csvData[count][num]+=1
		else:
			for info in sched.find_all(href=re.compile(find_all_value)):
				current_city=additional_checks2(list_to_check,info.text,y)
				if(current_city in info.text):	#increment for each city
					csvData[count][num]+=1









#extra cases
additionals=['Flushing','Bronx','Brooklyn','Manhattan','Queens','Staten Island']
city_count=0
citylist=[]
missing_data_exception(city_table)
missing_data_exception(stadium_table)
for link in city_table.find_all('tr'):
	#Each column count resets
	nl_football=0
	ml_baseball=0
	ml_soccer=0
	football=0
	baseball=0
	soccer=0
	current_city=""#one of the top cities 
	city_count=city_count+1
	if(city_count<7):#Max number of rows
		city = link.find('a')
		state=((city.find_next("a",title=True)))
		if (city.text != '[c]' and city!=None):#IN CASE WEB PAGE IS ALTERED
			for stadium_city in stadium_table.find_all('tr'):
				current_city=additional_checks(additionals,stadium_city.text,city.text,state.text)	
				if(current_city in stadium_city.text):
				#stadium_city.has_attr("style") is only used for major league
					if(stadium_city.has_attr("style")):
						if('Football' in stadium_city.text):
							nl_football+=1
						elif('Baseball' in stadium_city.text): 
							ml_baseball+=1
						elif('Soccer' in stadium_city.text):
							ml_soccer+=1
					else:
						if('Football' in stadium_city.text):
							football+=1
						elif('Baseball' in stadium_city.text): 
							baseball+=1
						elif('Soccer' in stadium_city.text):
							soccer+=1
				else:
					continue
			citylist.append(city.text)
			csvData.append([city.text,state.text,nl_football,ml_baseball,ml_soccer,football,baseball,soccer, 0, 0])
	else:
		break
		
		






additionals.append('New York, NY')# extra cases
additionals.append('Garden City')
scanner_one(comic_sched,citylist,8,additionals,'p')
scanner_one(dave_sched,citylist,9,additionals,"location")




csv_generator(csvData)
