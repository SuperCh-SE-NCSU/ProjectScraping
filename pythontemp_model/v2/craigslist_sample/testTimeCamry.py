from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings 
from scrapy import log, signals
from craigslist_sample.spiders.craig import MySpider
from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher
import datetime
from time import time

items=[]

def stop_reactor():
    reactor.stop()
def add_item(item):
    items.append(item)

dispatcher.connect(stop_reactor,signal=signals.spider_closed)
dispatcher.connect(add_item,signal=signals.item_passed)

previoustime=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M')
spider = MySpider(domain='craigslist.org',make='toyota',model='camry',starttime='2007',endtime='2010',minPrice=1000,maxPrice=12000,ctime=previoustime)
settings = get_project_settings()
crawler = Crawler(Settings())

crawler.configure()
crawler.crawl(spider)
crawler.start()

#log.start(logfile="results.log", loglevel=log.DEBUG, crawler=crawler, logstdout=False)
time1=time()
reactor.run()
time2=time()
for item in items:
    print item

print "seconds",time2-time1
print len(items)


#with open("results.log", "r") as f:
#    result = f.read()
#print result
