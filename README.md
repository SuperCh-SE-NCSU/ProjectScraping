
### Web Crawler Application  
[![Build Status](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping.svg?branch=master)](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping)

Using Scrapy to crawl craigslist and kbb to get sale information about used cars users specified and their kbb price.

### Background
A lot of people look at craigslist for an ideal used car that they are planing to buy or are just interested in. Normally when people look at the car price that listed on a craigslist page, they want to know if the car is worth the price listed. For people who are not car experters, they usually go to kbb to check the average price with the same specified conditions that are listed on craigslist. 

It's usually true that people will look through lots of cars on craigslist and check their kbb price time and time again. It could takes several days, or several weeks before they find their ideal car.

Sometimes, a good car is just posted to craigslist, which is exactly the car a person want. But he isbusy with your work or being tangled with some personal thins and forget to check craigslist, he may miss the car.
If there is some service that can send emails to him which notify him of a newly posted car, he won't miss it.

### Goals
Our goal is to offer a mailing service to people who are looking at craigslist for used car, providing a craigslist link to the car that they have expressed their interests in from our subscribing website and the kbb price for the specific car.

To be To be more specific, we develop a website for people to subscribe to our email service and get car information that they specified.(car model, year of make, mileage,etc)Based on these information, we crawl craiglist and find the right car, which agree with the customer¡¯s needs and look up the price for the car from Kbb. Then we will email subscribed customers the information they need: the basic information( such as year, make, mileage,price), a link to the original posts on craiglist, and the price from Kbb.
There should be two versions of our application.

Version_1: Minimal functionality. According to customers' need specified on our subscription website, send them emails including information that they need from 2 websites, Craglist and kbb.(work done)

Version_2: Full functionality. Besides the subscription service, Build a database of customers login information and search records and extend the functionality of our website, so that everytime customer login our website, they will get latest car information since last login. (Future work)

### Methods
1.A basic website is developed for users to subscribe to our email notification service 

2.postgresql is used to store subscribed user information.

3.A web crawler is used to craw craigslist and kbb for car informations.

4.[Sendgrid](https://sendgrid.com/home-two) is used for email delivery service.

**Introduction to web crawler**

A Web crawler is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing. A Web crawler may also be called a Web spider, an ant, an automatic indexer, or (in the FOAF software context) a Web scutter.

Web search engines and some other sites use Web crawling or spidering software to update their web content or indexes of others sites' web content. Web crawlers can copy all the pages they visit for later processing by a search engine that indexes the downloaded pages so that users can search them much more quickly.

Crawlers can validate hyperlinks and HTML code. They can also be used for web scraping (see also data-driven programming).

### Design
<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/ProjectScraping--design.png">

User can choose different restrictions (car model, car make, year,  price and email) and subscribe our daily email. We will keep users' personal information in PostgreSQL database and ensure safety. Then we try to use different crawler engine (regular regression, beautifulsoup and scrapy) to obtain latest information users need on Craglist and kbb and send email daily.

### Implementation
<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/ProjectScraping--implement.png">

When clicking "subscribe" button, the main process will write user's information into database immediately,  and a sub process will generate simultaneously. The sub process will send a welcome email to user. The first email only include available cars in Craglist, so it will be very fast.

There is also a send email process on our server. This process is a 24/7 service, and everyday it will send emails to each subscribers. The content of emails comes from crawler engine.

### Platform and optimization trial
- At very begining, we tried to put our system on Heroku and Amazon web services. However, after deploy our system on these two platform, we found that craglist and kbb block the IP address of these two companies, and we cannot crawl any information. So we change to NCSU VCL now.

- In order to increase the speed of crawling, we decided to build another local database to store crawling results. But after deep consideration, we find this database is useless. There are several reasons:
   - Content send to subscribers must be latest, so store obsolete into database is useless;
   - If we build this database, we have to update it daily. Because we cannot access their databases, so the only method is still crawling. What is more, it is unrealisitic to store all information locally.

### Test procedure
   To be completed
   
### Completeness of the tests
   To be completed

### Result
The following website is developed for people to subscribe to our email notification service.
http://152.46.17.210:8080/<br/>

<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/pythontemp_model/img/subscribe.png">

We tested the functionality by subscribe with different car information specified.We received the email. Then we checked craigslist and found that all the cars satisfying the condition are included in the email.

### Disscussion
**1.Advantages of this application**

Right now, people have to go to craiglist to find the car they are interested in with a posted price, and then go to kbb, checking out the review price.It is a pain to look up the kbb price for different cars again and again. Our application will do these two jobs for customers automatically, and people can get updated information emailed to them everyday so they won't miss a newly added target.

**2.Difficulty during deploying the application**

We tried deploying the application to Heroku, but the IP of heroku is blocked by craigslist. Craigslist seems to block all the IPs from commercial servers.

### Conclusion

Web crawler is a powerful tool which makes gathering information from webpage more easier, but some websites will block commercial servers from crawling websites to protect their copyright.

### Future Work
1. Achieve full functionality in version 2.
2. A server is needed to long-time service.
3. The information sending to users could be beautified into a table, with pictures.

### Reference
1.Shaw, Zed A. "Learn Python the hard way." (2010).
2.https://github.com/scrapy/scrapy
3.https://github.com/scrapy/scrapy/wiki
4.https://doc.scrapy.org/en/latest/




