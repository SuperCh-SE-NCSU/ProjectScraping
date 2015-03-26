from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
from scrapy.http import Request
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
            item ["carlink"] = "http://raleigh.craigslist.org/"+str(L.pop())
          item ["abstractInformation"] =str(list(title.xpath(".//a[@class='hdrlnk']/text()").extract()).pop())
          item ["timePost"]=str(list(title.xpath(".//span[@class='pl']/time/@datetime").extract()).pop())
         
          L=title.xpath(".//span[@class='price'][1]/text()").extract()
          if len(L)>0:
             item ["price"]= str(L.pop())
          try:
            #milageandy=getMilageAndYear(item ["carlink"])
            item ["mileagel"]=milageandy['milage']
            item ["caryear"]=milageandy['year']
          except:
            item ["mileagel"]='0'
            item ["caryear"]='0'
            
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
