# MajorCityEntertainment
MajorCitySports is a web-scraping application devoted for Topos.ai 
for examining if there are major differences between top cities through entertainment 
by generating a csv(output.csv) to allow for easier visualization of the 
data(mainly numerical)

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
Does the number of times a comedy celebrity visits a city emphasize difference between cities?
Ver 3.0, adds a more specific data set by helping to view 
the number of times a celebrity such as Dave Chapelle has visited each of these cities. 


## Ver 4.0(Current Version): Adding number of times Ariana Grande had an event
Does the number of times a music celebrity visits 
a city emphasize difference between cities?
Ver 4.0, helps view the number
of times a celebrity such as Ariana Grande has visited each of these cities. 



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

7. Ariana Grande Events: Can obtain information from multiple pages with little changes to
the scanner_one algorithm 



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


## Functions

scanner_one: a function to scan similar web pages in a similar fashion 

missing_data_exception: used to check if missing the expected html value, exit program 

additional_checks: checks for villages/boroughs within a city

csv_generator: generates csv with given rows 



## Example

Stadiums Results: At first glance, the number of sports stadiums opened
vary greatly for each major city, except Phoenix most likely due to most stadiums 
being outside of the city itself

Comic-Con Results: New York City seems to have the most Comic-cons while 
Phoenix is shown to not have any at all. 

Dave Chapelle Shows: From this example, it seems New York and Houston have more  
Dave Chapelle Events while other cities have very little. 

Ariana Grande: It also appears that Ariana Grande appears a lot in New York City.

So far New York City is shown to be the most different compared to the other cities
in the number of comic-cons it hosts every year
while still hosting comedians such as Dave Chapelle and 
singers such as Ariana Grande according to the data so far.

However, a conclusion can't be truly given on whether their is a major difference
between cities since data sets and web site sources such as
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

**NOTE 5:** Comic-con data, Dave Chapelle Events, and Ariana Grande 
do not come from wikipedia 




