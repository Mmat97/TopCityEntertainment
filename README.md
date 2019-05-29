# MajorCityEntertainment
MajorCitySports is a web-scraping application devoted for Topos.ai 
to examine major differences between top cities through entertainment 
by generating a csv(output.csv) allowing easier visualization of the 
data(mainly numerical)

## Description
MajorCityEntertainment makes use of more than one web page to go past basic city 
information and go more specifically into entertainment culture to see what makes cities
unique


## Ver 1.0: Cities, Sport Stadiums Built
Is there a major difference between top cities in the number of stadiums a city's sports team/tenant establishes its residency?(Examines built stadiums associated with each city)

## Ver 2.0: Adding Comic - Cons
Is there a difference expressed between top cities when accounting for the number of comic-cons they have?

## Ver 3.0: Adding number of times Dave Chapelle had an event
Is there a difference expressed between top cities 
when accounting for the number of Dave Chapelle Live Events they have?


## Ver 4.0(Current Version): Adding number of times Ariana Grande had an event
Is there a difference expressed between top cities
when accounting for the number of Ariana Grande Live Events they have? 



## Advantages
1. Scans and analyzes more than one table on the web

2. Focuses on amounts so can be transferred easily to a bar graph 

3. Generates a csv file which can be analyzed alongside other data to see how 
a variety of entertainment can have an impact on a neighborhood's culture

4. Sport Stadiums: Separates Major League owned Stadiums and non-Major League owned Stadiums 

5. Comic-Cons: Captures data regarding upcoming comic-cons from a list and not just a table 

6. Dave Chapelle Events: Focuses on location links to match with major cities that we
are currently examining 

7. Ariana Grande Events: Can obtain information from multiple pages with little changes to
the scrape_other_urls function

8. The code itself doesn't involve changing variables globally and instead uses call
by value while returning the value edited(mainly for csvData)

9. The amount of cities examined can be changed with the limit variable


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

csv_generator: generates csv with given rows 

scraper: base scraping algorithm where the class values are set

hasNum: function mainly used to disregard non-city names values for 
the U.S. cities

additional_checks: checks for villages/boroughs within a city

scrape_city_and_states: returns a list of tuples(cityx,statex) for a number of cities
equal to the limit variable  

scrape_stadiums: edits and returns edits csv data after examining data from 
list of stadiums page

scrape_comic_or_concerts: edits and returns edits csv data after examining data from 
Comic Con, Dave Chapelle, and ariana Grande Schedules 

scrape_other_urls: function to decide which scraper function is best suited for the given
parameters 


## Example
<img width="1280" alt="Screen Shot 2019-05-29 at 6 08 44 PM" src="https://user-images.githubusercontent.com/13366041/58594866-d8e44d00-823c-11e9-8dd6-f95e2cf8a0de.png">


Stadiums Results: The number of sports stadiums within the metropolitan area for each sport 
vary greatly for each major city, except for Phoenix with the least. The NFL's Arizona Cardinals do not establish their residency in Phoenix, although the stadium is located in the metropolitan area, which contributes to its outlier position.

Comic-Con Results: New York City seems to have the most Comic-cons while 
Phoenix is shown to not have any at all. 

Dave Chapelle Shows: From this example, it suggests New York and Houston have more  
Dave Chapelle Events while other cities have very little. 

Ariana Grande: Data suggests that Ariana Grande performs frequently live in New York City.

From this example, it seems that New York City and Phoenix appear to be the most different.
However, a conclusion can't be formulated since web site sources such as
Wikipedia do not always provide valid estimates and there may be outliers that have yet to be examined. 



## Important Notes:

**NOTE 1:** Adding state in first column since there can be more than
one city with the same name
Ex: Manhattan, NY vs. Manhattan, KS

**NOTE 2:** A stadium is counted for certain city also when a sport 
tenant/team from that city establishes its residency at the stadium 

**NOTE 3:** The stadiums focused on include stadiums that were 
renovated and/or closed down 

**NOTE 4:** Currently focusing on Football, Soccer and Baseball stadiums 

**NOTE 5:** Comic-cons, Dave Chapelle Events, and Ariana Grande Events
do not come from wikipedia 




