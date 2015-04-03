from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings 
from scrapy import log, signals
from spiders.craig import MySpider
from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()
dispathcer.connect(stop_reactor,signal=signals.spider_closed)
spider = MySpider(domain='craigslist.org')
settings = get_project_settings()
crawler = Crawler(Settings())

crawler.configure()
crawler.crawl(spider)
crawler.start()

log.start(logfile="results.log", loglevel=log.DEBUG, crawler=crawler, logstdout=False)

reactor.run()

with open("results.log", "r") as f:
    result = f.read()
print result
