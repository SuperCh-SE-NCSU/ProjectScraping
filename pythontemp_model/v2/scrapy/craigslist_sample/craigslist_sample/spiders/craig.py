from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
import datetime
import urllib2
import re

def getMilageAndYear(url):
    response = urllib2.urlopen(url)
    html = response.read()
    #print html
    try:
        terms=re.search('<span>odometer:\s*<b>(\d*)</b></span>',html)
        odometer=terms.group(1)
    except:
        odometer='0'
    try:
        terms=re.search('<p\s*class="attrgroup"><span><b>(\d*)',html)
        year=terms.group(1)
    except:
        year='0'
    milageandy={'milage':odometer,'year':year}
    return milageandy
            

class MySpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://raleigh.craigslist.org/search/cto"]
  max_cid=24
 
  make='toyota'
  model='camry'
  starttime='2007'
  endtime='2009'
  minPrice=1000
  maxPrice=10000
  ctime=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M')
  
  def start_requests(self):
    for i in range(self.max_cid):
      yield Request('http://raleigh.craigslist.org/search/cto?s=%d'%(i*100),callback=self.parse)
                    
  def parse(self, response):
      
      
      hxs = HtmlXPathSelector(response)
      
      titles = hxs.xpath('//p[@class="row"]')
      
      items = []
      for title in titles:
          # structure of spider
          # <p class="row" data-pid="4947366935"> <a href="/cto/4947366935.html" class="i"
          # data-ids="0:00d0d_45lNsxzKpKi"><span class="price">&#x0024;2500</span></a> <span class="txt">
          # <span class="star"></span> <span class="pl"> <time datetime="2015-03-24 16:25" title="Tue 24 Mar
          # 04:25:35 PM (7 minutes ago)">Mar 24</time> <a href="/cto/4947366935.html" data-id="4947366935"
          # data-repost-of="3855891772" class="hdrlnk">1995 Toyota Camry</a> </span> <span class="l2">
          # <span class="price">&#x0024;2500</span> <span class="pnr"> <small> (Chapel Hill)</small>
          # <span class="px"> <span class="p"> pic</span></span> </span> </span> </span> </p>
          
          #timePost,price,carlink,abstractInformation,mileagel,modle,caryear
          item = CraigslistSampleItem()
          L =title.xpath(".//a/@href").extract()
          if len(L)>0:
            item ["carlink"] = "http://raleigh.craigslist.org/"+L.pop().encode('ascii', 'ignore')
          else:
            item["carlink"]="unknown"
    
          item ["abstractInformation"] =(list(title.xpath(".//a[@class='hdrlnk']/text()").extract()).pop()).encode('ascii', 'ignore')
          item ["timePost"]=(list(title.xpath(".//span[@class='pl']/time/@datetime").extract()).pop()).encode('ascii', 'ignore')
         
          L=title.xpath(".//span[@class='price'][1]/text()").extract()
          if len(L)>0:
             item["price"]= (L.pop()).encode('ascii', 'ignore')
          else:
             item["price"]='0'
          item["price"]=int(item["price"].replace('$',''))
          
          if item["price"]>=self.minPrice and item["price"]<=self.maxPrice and self.model in item["abstractInformation"].lower():
              try:
                milageandy=getMilageAndYear(item ["carlink"])
                item ["mileagel"]=milageandy['milage']
                item ["caryear"]=milageandy['year']
              except:
                item ["mileagel"]='0'
                item ["caryear"]='0'
            
              if item["timePost"]<self.ctime:
                  raise CloseSpider('bandwidth_exceeded')
              
              if item ["caryear"]>=self.starttime and item ["caryear"]<=self.endtime:
                  items.append(item)
      
      return items

  def getMilageAndYear(self,response):
    hxs=HtmlXPathSelector(response)
    try:
      terms=hxs.xpath('//span/odometer/b/text()').extract()
      odometer=terms.group(1)
    except:
      odometer='0'
    try:
      year=re.search('\d*',str(hxs.xpath("//p[@class='attrgroup'/span/b/text()").extract()))
    except:
      year='0'
    milageandy={'milage':odometer,'year':year}
    return milageandy
