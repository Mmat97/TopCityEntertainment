import csv
import requests
from bs4 import BeautifulSoup

  
#Retrieve Data and parse in to html for each web page specified
url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 
tb = soup.find("table", class_ = "wikitable sortable")
url2="https://en.wikipedia.org/wiki/List_of_U.S._stadiums_by_capacity"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')
stadium_table = soup2.find("table", class_ = "wikitable sortable")



#Initialize csv with columns 
	#NL_Football=NFL owned stadium
	#ML_Baseball=MLB owned stadium
	#ML_Soccer=MLS owned stadium
csvData=[['City', 'State','NL_Football','ML_Baseball','ML_Soccer','football','baseball','soccer']]

def csv_generator(csvData):
	with open('output.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
	csvFile.close()

	


def additional_checks(other_cities_list, parsed_text, city_name,current_state):
	for x in other_cities_list:
		if((x in parsed_text) and (current_state in parsed_text)):
			return x
	return city_name




additionals=['Flushing','Bronx','Brooklyn','Manhattan','Queens','Staten Island']
city_count=0
for link in tb.find_all('tr'):
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
		if (city.text != '[c]' ):
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
			csvData.append([city.text,state.text,nl_football,ml_baseball,ml_soccer,football,baseball,soccer])
	else:
		break
		
	csv_generator(csvData)
