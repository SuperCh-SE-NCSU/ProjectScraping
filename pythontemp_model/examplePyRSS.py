import datetime
import PyRSS2Gen
import xml.etree.ElementTree as ET
import time

rss = PyRSS2Gen.RSS2(
    title = "Car Info",
    link = "http://www.dalkescientific.com/Python/PyRSS2Gen.html",
    description = "the result of crawler",

    mystrTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    lastBuildDate = datetime.datetime.now(),

    items = [
       PyRSS2Gen.RSSItem(
         title = "model",
         link = "",
         description = "car model",
         guid = PyRSS2Gen.Guid("http://www.dalkescientific.com/news/"
                          "030906-PyRSS2Gen.html"),
         pubDate = datetime.datetime(2015, 2, 10, 17, 00)),
       PyRSS2Gen.RSSItem(
         title = "year",
         link = "",
         description = "product year",
         guid = PyRSS2Gen.Guid("http://www.dalkescientific.com/writings/"
                               "diary/archive/2003/09/06/RSS.html"),
         pubDate = datetime.datetime(2015, 2, 10, 17, 01)),
       PyRSS2Gen.RSSItem(
         title = "mile",
         link = "",
         description = "travel mile",
         guid = PyRSS2Gen.Guid("http://www.dalkescientific.com/writings/"
                               "diary/archive/2003/09/06/RSS.html"),
         pubDate = datetime.datetime(2015, 2, 10, 17, 02)),
    ])

rss.write_xml(open("car_info.xml", "w"))
