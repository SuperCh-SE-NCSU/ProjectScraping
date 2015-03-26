
### Web Crawler Application  
[![Build Status](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping.svg?branch=master)](https://travis-ci.org/SuperCh-SE-NCSU/ProjectScraping)

Using Scrapy to crawl craigslist and kbb to get sale information about used cars users specified and their kbb price.

Users can subscribe to our email service.We will send them the lastest car information they need once per day. 
### Demo

http://152.46.17.210:8080/<br/>
<img align=left src="https://github.com/SuperCh-SE-NCSU/ProjectScraping/doc/stress_test.png" style="float:left;with:100px;height:300px">
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

