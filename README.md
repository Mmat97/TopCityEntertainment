# MajorCityEntertainment
MajorCitySports is a web-scraping application devoted for Topos.ai 
for examining the differences between major cities through entertainment by generating 
a csv(output.csv) to allow for easier visualization of the data 

## Description
MajorCityEntertainment makes use of more than one web page to go past basic city 
information and go more specifically into entertainment culture to see what makes a city
unique


## Ver 1.0: Cities, Sport Stadiums Built
Is there a major difference for top cities in the number of stadiums for each sport
that they have? The application currently obtains the names of the most populous cities
and the number of stadiums opened for sports such as Football,
Soccer and Baseball corresponding to those cities to examine if there is 
a similar trend or not.


## Ver 2.0: Adding Comic - Cons
Going beyond stadiums, ver 2.0 will check if there is a relationship between
stadiums and the number of ACTIVE comic-cons along with if the number of comic-cons 
is unique for each city. 

## Ver 3.0: Adding number of times Dave Chapelle had an event
Does the number of times a celebrity visits a city emphasize difference between cities?
Ver 3.0, adds a more specific data set by viewing the number of times a celebrity such as Dave 
Chapelle has visited each of these cities. 



## Advantages
1.Scans and analyzes more than one table on the web
2. Focuses on amounts so can be transferred easily to a bar graph 
3. Generates a csv file which can be analyzed alongside other data to see how 
a variety of entertainment can have an impact on a neighborhood's culture
4. Sport Stadiums: Separates Major League owned Stadiums and non-Major League owned Stadiums
5. Comic-Cons: Captures data regarding upcoming comic-cons from 
a list and not just a table 
6. Dave Chapelle Events: Focuses on location links to match with major cities that we
are currently examining 



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


## Installation and how to Run 
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



## Example

Stadiums Results: At first glance, the number of sports stadiums opened
vary greatly for each major city.


Comic-Con Results: From this example, each major city seems to have the same or a close 
number of comic-cons.

Dave Chapelle Shows: From this example, it seems New York and Houston have more  
Dave Chapelle Events 

However, a conclusion can't be truly given on whether their is a relationship 
between cities or certain data sets as the web site sources such as
wikipedia do not always give valid estimates 
and there may be outliers that have yet to be examined. 

The csv is generated in the proper format, however,
allowing for more in-depth visualization and analysis. 

## Important Notes:

**NOTE 1:** Adding state column since there can be more than
one city with the same name
Ex: Manhattan, NY vs. Manhattan, KS

**NOTE 2:** A stadium is counted for certain city also when a sport 
tenant/team from that city owns the stadium 

**NOTE 3:** The stadiums focused on include stadiums that were 
renovated and/or closed down 

**NOTE 4:** Currently focusing on Football, Soccer and Baseball stadiums 

**NOTE 5:** Comic-con data and Dave Chapelle Events do not come from wikipedia 




