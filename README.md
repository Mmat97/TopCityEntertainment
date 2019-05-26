# MajorCityEntertainment
MajorCitySports is a web-scraping application devoted for Topos.ai 
for obtaining datasets on different entertainment to see what makes a major city unique 

## Description
MajorCityEntertainment makes use of more than one wikipedia page to go past basic city 
information and go more specifically into entertainment

## Ver 1.0: Sport Stadiums 

Is there a similar trend for major cities in the number of stadiums for each sport
that they have? The application currently obtains the names of the most populous cities
and the number of stadiums opened for sports such as Football,
Soccer and Baseball corresponding to those cities to examine if this is true or not.


## Ver 2.0(Under Construction): Comic - Cons
Going beyond stadiums, ver 2.0 will check if there is a connection between
stadiums and the number of ACTIVE comic-cons along with if the number of comic-cons 
vary between major cities. 


## Advantages
1.Scans and analyzes two different tables on the web
2. Generates a csv file which can be analyzed alongside other data to see how 
a variety of entertainment can have an impact on a neighborhood's culture
3. Sport Stadiums: Separates Major League owned Stadiums and non-Major League owned Stadiums



## Tools/Languages/References
**Language:** 

-Python Version 2.7
[Python Website](https://www.python.org/)

**Libraries:** 

-Beautiful Soup
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

-Requests
[Requests](https://pypi.org/project/requests/2.7.0/)

**OS Used:** 

-Mac OS(Terminal)


## Installation and Run Example
**Install:** 

```
	pip install python-csv
```

```
	pip install wikipedia
```

```
	pip install requests
```

```
	pip install beautifulsoup4
```

**Run:** 

In terminal, once in the directory where the csv_generate.py file is located,type:

```
	python csv_generate.py
```


A file named, output.csv(specified in the code) will be created in the proper csv format 


## Important Notes:

**NOTE 1:** Adding state column since there can be more than
one city with the same name
Ex: Manhattan, NY vs. Manhattan, KS

**NOTE 2:** A stadium is counted for certain city also when a sport 
tenant/team from that city owns the stadium 

**NOTE 3:** The stadiums focused on include stadiums that were 
renovated and/or closed down 

**NOTE 4:** Currently focusing on Football, Soccer and Baseball stadiums. May add 
Tennis, Racing, and multi-purpose stadiums in a later version. 
	
## Possible Additions 
1. Adding other sources and add more recent and accurate data to the set since 
Wikipedia can often lack in this.
2.Focus only on closed down stadiums 
3. Adding data sets on other forms of entertainment
4. Displaying data as a bar graph to make it more easier to visualize
5. Adding data sets to examine changes under a span of time and not just amounts
6. Add more edge cases in case of altered or deleted data 





