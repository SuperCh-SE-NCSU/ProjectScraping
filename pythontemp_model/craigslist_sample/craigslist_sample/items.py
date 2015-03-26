# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
  timePost = Field()
  price = Field()
  carlink=Field()
  abstractInformation=Field()
  mileagel=Field()
  #model=Field()
  caryear=Field()
  pricetype=Field()
