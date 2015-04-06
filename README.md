
# Web Crawler Application  
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

#### Introduction to web crawler

A Web crawler is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing. A Web crawler may also be called a Web spider, an ant, an automatic indexer, or (in the FOAF software context) a Web scutter.

Web search engines and some other sites use Web crawling or spidering software to update their web content or indexes of others sites' web content. Web crawlers can copy all the pages they visit for later processing by a search engine that indexes the downloaded pages so that users can search them much more quickly.

Crawlers can validate hyperlinks and HTML code. They can also be used for web scraping (see also data-driven programming).

### Design and Pattern
<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/ProjectScraping--design.png">

User can choose different restrictions (car model, car make, year,  price and email) and subscribe our daily email. We will keep users' personal information in PostgreSQL database and ensure safety. Then we try to use different crawler engine (regular regression, beautifulsoup and scrapy) to obtain latest information users need on Craglist and kbb and send email daily.

#### Public-subscribe design pattern
We also use public-subscribe design pattern. We build  a one-to-many dependence between our system and subscribers. And when we collect latest car information and send email daily, all subscribers are notified by emails.
   - Public-subscribe design pattern alerts other objects’ changes without rebuilding dependencies on them. The individual views implement the Observer interface and register with the model. The model tracks the list of all observers that subscribe to changes. When a model changes, the model iterates through all registered observers and notifies them of the change. With this approach, the model never requires specific information about any views.

### File system architecture
- ProjectScraping:
   - Web.py initial directory.
- bin:
   - Executable file of web application.
- doc:
   - Related images and documents.
- pythontemp_model:
   - All historical versions of python files and test files. These files do not execute when application running.
- static:
   - Javascript, css and csv files.
- templates:
   - Website html files.
- tests:
   - All test files.

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
   - We tested the functionality by subscribe with different car information specified.We received the email. Then we checked craigslist and found that all the cars satisfying the condition are included in the email.

### Result
- The following website is developed for people to subscribe to our email notification service.
http://152.46.17.210:8080/<br/>

<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/subscribe.png">

- In following video, we display follow issues:
   - https://www.youtube.com/watch?v=Bmi7bwp5V7k&feature=youtu.be
   - User first subscribes our email service. 
   - Then user receives a welcome email including available cars in Craglist immediately.
   - User try to compare the time of manual searching on two website and our web email service.
   - The video shows that user receives second email before he finish manual search.
   - The second email includes information of available cars on Craglist and completed car prices on kbb.
   - Actually, second email is the service about sending latest information daily. In this video, in order to minimise the time, we set daily email 2 minutes after subscribe.


### Disscussion
**1.Advantages of this application**

Right now, people have to go to craiglist to find the car they are interested in with a posted price, and then go to kbb, checking out the review price.It is a pain to look up the kbb price for different cars again and again. Our application will do these two jobs for customers automatically, and people can get updated information emailed to them everyday so they won't miss a newly added target.

**2.Difficulty during deploying the application**

We tried deploying the application to Heroku and Amazon web services. But the IP of those two is blocked by craigslist. Craigslist seems to block all the IPs from commercial servers. We used VCL to solve this problem.

**3.Comparison between python regular regression, beautiful soup and scrapy**
In theory, regular expressions are a powerful language for matching text patterns. The Python "re" module provides regular expression support. BeautifulSoup is a parsing library and scrapy is a web scraper framework. You give Scrapy a root URL to start crawling, then you can specify constraints on how many number of URLs you want to crawl and fetch,etc., It is a complete framework for Web-scrapping or crawling.
 In practice, we can use all those three tools. Python regular expressions is flexible and easy to employ.While scrapy and beautiful soup are much more robust. Also, scrapy framework supplies some functions like sending emails. We develop all those three methods and we are interested in the eff compare the time to crawl four specific models of cars from craiglist using those different methods. The result is is shown in the following figure.
<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/craigslisttimeComparison.png">

From the above figure, we know that python regular expression and scrape framework are faster than beautiful soup. But python regular expression is not robust to the changing of the html structure. Sometime it will miss specific cars. 

 
  

### Conclusion

**1. Web crawling**

Web crawler is a powerful tool to gather information from webpage. It will save people a lot of time when searching for information from a complicate webpage, which has a lot of information. It is good for personal use,running on local server. But when you deploy it on some online server, problems appear.
 
It has been proved true that some websites will block commercial servers from crawling their web,which is quite predictable. These websites are commercial websites,too. Even though they might be free for people to browse, they need users watch their supporters'commercial advertisement to survive. To protect their interests, they have to block others crawl their webpages. 

Thirdly, the legality of scraping, especially for commercial use is not clear now. Web scraping may be against the terms of use of some websites. The enforceability of these terms is unclear[6].

But except for these limitations, web crawling is quite useful for information gathering. 

**2. Github**
We use github to do version control and publish issues. This is our first time to collobrate working in gituhub.  We also find some silimar projects in github like scrape-kbb.  


### Future Work

**1. Reduce scraping time of KBB**

In practice, we find the time to scrape the prices of kbb is very long. We find a method to reduce scraping time. In the older method, we need to scrape the types of models recursively. That means, we need to firstly scrape the model page and find the types in those models, then we can get the links of each time, scrape the price of each type. However, if we know the types of each model in advance. We can visit the url of each type directly by passing the parameters. We compare those two methods in the following figure
<img align=center src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/blob/master/doc/kbbtimeComparison.png">
The new method reduce the scraping time of KBB by five times. That's wonderful! But now we are struggling in getting the types of each model in different years. We will integrate the new method in our future work. 

**2. Achieve full functionality in version 2.**

In more detail, we could make out website having more functionalities.Apart from subscription,It will show the car information crawled from craigslist and Kbb right after you click the submit button.

It will show people's browsing history, just like amazon.

**3. A server is needed to long-time service.**

Our initial attempt to deploy our application to Heroku, AWS failed since craigslist blocks Heroku and AWS's IPs. For long-time service, we need a online server instead of a VCL machine.

**4. The information sended to users could be stored and beautified into a table, with pictures.**

It will include one car'picture in the car information that is displayed on our web or sent to perple's emails. The whole thing could be put into a table, making it look like a beautiful post.

### Reference
1.Shaw, Zed A. "Learn Python the hard way." (2010).<br/>
2.https://github.com/scrapy/scrapy<br/>
3.https://github.com/scrapy/scrapy/wiki<br/>
4.https://doc.scrapy.org/en/latest/<br/>
5.http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern
6."FAQ about linking – Are website terms of use binding contracts?". www.chillingeffects.org. 2007-08-20. Retrieved 2007-08-20.
7.https://github.com/storrgie/scrape-kbb



