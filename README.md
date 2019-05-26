# MajorCitySports
MajorCitySports is a web-scraping application for obtaining the number of stadiums of 
different sports for the major cities in the U.S.

## Description
MajorCitySports makes use of more than one wikipedia page to go past basic city information 
and go more specially into the sports culture. The application currently obtains the 
names of the most populous cities and the number of stadiums for sports such as 
Football, Soccer and Baseball corresponding to those cities. 


## Advantages
1.Scans two different tables on the web
2. Generates a csv file which can be analyzed alongside other data to see how 
a variety of stadium sports can have an impact on a neighborhood's culture
3. Separates Major League owned Stadiums 



## Tools/Languages/References
**Languages:** 
Python
[Python Website](https://www.python.org/)

**Libraries:** 
Beautiful Soup
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Requests
[Requests](https://pypi.org/project/requests/2.7.0/)

**OS Used:** 
Mac OS(Terminal)


## Installation and Run Example
**Install:** 
'''html
	pip install python-csv
'''

'''html
	pip install wikipedia
'''

'''html
	pip install requests
'''

'''html
	pip install beautifulsoup4
'''
**Run:** 
In terminal, once in the directory where the csv_generate.py file is located,type:
'''html
	python csv_generate.py
'''

A file named, output.csv(specified in the code) will be created in the proper csv format 


##Important Notes:
**NOTE 1:** Adding state column since there can be more than
one city with the same name
Ex: Manhattan, NY vs. Manhattan, KS

**NOTE 2:** A stadium is counted for certain city also when a sport 
tenant/team from that city owns the stadium 

**NOTE 3:** Currently focusing on Football, Soccer and Baseball stadiums. May add 
Tennis, Racing, and multi-purpose stadiums in a later version. 
	
## Next Steps 
1. I hope to use other sources and add more recent/accurate data to the set since Wikipedia 
	can often lack in this.



