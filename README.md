
### Web Crawler Application  
[![Build Status](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping.svg?branch=master)](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping)

Using Scrapy to crawl craigslist and kbb to get sale information about used cars users specified and their kbb price.

### Goals
Our goal is to offer a mailing service to people who are looking at craigslist for used car, providing a craigslist link to the car that they have expressed their interests in from our subscribing website and the kbb price for the specific car.

### Background
A lot of people look at craigslist for an ideal used car that they are planing to buy or are just interested in. Normally when people look at the car price that listed on a craigslist page, they want to know if the car is worth the price listed. For people who are not car experters, they usually go to kbb to check the average price with the same specified conditions that are listed on craigslist. 

It's usually true that people will look through lots of cars on craigslist and check their kbb price time and time again. It could takes several days, or several weeks before they find their ideal car.

Sometimes, a good car is just posted to craigslist, which is exactly the car a person want. But he isbusy with your work or being tangled with some personal thins and forget to check craigslist, he may miss the car.
If there is some service that can send emails to him which notify him of a newly posted car, he won't miss it.

### Methods
1.A basic website is developed for users to subscribe to our email notification service 

2.postgresql is used to store subscribed user information.

3.A web crawler is used to craw craigslist and kbb for car informations.

4.[Sendgrid](https://sendgrid.com/home-two) is used for email delivery service.


**Introduction to web crawler**

A Web crawler is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing. A Web crawler may also be called a Web spider, an ant, an automatic indexer, or (in the FOAF software context) a Web scutter.

Web search engines and some other sites use Web crawling or spidering software to update their web content or indexes of others sites' web content. Web crawlers can copy all the pages they visit for later processing by a search engine that indexes the downloaded pages so that users can search them much more quickly.

Crawlers can validate hyperlinks and HTML code. They can also be used for web scraping (see also data-driven programming).


### Result
The following website is developed for people to subscribe to our email notification service.
http://152.46.17.210:8080/<br/>
<img align=left src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/pythontemp_model/img/subscribe.png" style="float:left;with:100px;height:300px">



### Disscussion

1.We tested the functionality by subscribe with different car information specified.We received the email. Then we checked craigslist and found that all the cars satisfying the condition are included in the email.

2.We tried deploying the application to Heroku, but the IP of heroku is blocked by craigslist. Craigslist seems to block all the IPs from commercial servers.

3.Time Comparision of three different mehtods
<img align=left src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/ProjectScraping/doc/timeComparison.png" style="float:left;with:100px;height:300px">
### Conclusion


### Future Work
1. A server is needed to long-time service.
2. the information sending to users could be beautified to a table, with pictures.
### Reference
### Demo

### Install 3rd part library (needed for subscription)

```
sudo pip install lpthw.web
```   

### Develop Phase

  (1).  Crawl craigslist to get sale price and other information about used cars users specified and send the information to subscribed users's emails (completed)

  (2).  Set parameters to get the price from kbb (demo, to be implemented in a function)

  (3).  Integrate part 1 and part 2 to form the information which will be sended to users (partly completed)

  (4).  Rewrite 1,2,3 in scrapy (to do)
  
  (5).  Build a website for users to subscribe to our email service (completed)
  
  (6).  Get data from a dynamic website (done)

  (7).  Complete the whole system and compare the two different strategies (to do)

