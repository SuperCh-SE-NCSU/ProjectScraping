import urllib2
import re
import time
import xml.etree.ElementTree as ET
#This file contains the basic crawl function for craigslist.
class carlist:
    def __init__(self,modellist,pricelist,carlinklist,abstractIlist,mileagel,timepostlist,caryear):
        self.modellist=modellist
        self.pricelist=pricelist
        self.carlinklist=carlinklist
        self.abstractIlist=abstractIlist
        self.timepostlist=timepostlist
        self.mileagel=mileagel
        self.year=caryear

    
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
        

def craglistsearch(cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime):
    model=list()
    price=list()
    carlink=list()
    abstractInformation=list()
    mileagel=list()
    caryear=list()
    
    timePost=list()
    today=True
    num=0
    mystrTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    print mystrTime
    print cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime
    while today:
        try:
            if num==0:
                tempstr='http://raleigh.craigslist.org/search/cto//'
            else:
                tempstr='http://raleigh.craigslist.org/search/cto?s='+str(num)+'//'
    
            response = urllib2.urlopen(tempstr)
            html = response.read()


            Terms8=re.findall(r'<span class="txt"> <span class="star"></span> <span class="pl"> <time\s*datetime=".+?" title=".+?">.+?</time> <a href=".+?"\s*data-id="\w+"\s*class="\w+">.+?</a>\s*</span>\s*<span\s*class="l2"> .+?</p>',html)
            if not Terms8:
                today=False
                break
            for i in range(len(Terms8)):
                timeCur=re.search(r'<time\s*datetime="(.+?)" title="(.+?)">(.+?)</time> <a href="(.+?)"\s*data-id="(\w+)"\s*class="(\w+)">(.+?)</a>\s*</span>\s*<span\s*class="l2">\s*<span\s*?class="price">&#x0024;(\w+?)</span>',Terms8[i])
                if timeCur:
                  
                    if timeCur.group(1)<=ctime:
                        today=False
                        break
                
                    if cmodel in timeCur.group(7).lower() and int(timeCur.group(8))>=cminprice and int(timeCur.group(8))<=cmaxprice:
                        milandyear=getMilageAndYear('http://raleigh.craigslist.org'+timeCur.group(4))
                        #print milandyear
                        if milandyear['year']>=cstartyear and milandyear['year']<=cendyear:
                            #print milandyear['year']
                            timePost.append(timeCur.group(3))
                            price.append(timeCur.group(8))
                            carlink.append(timeCur.group(4))
                            abstractInformation.append(timeCur.group(7))
                            mileagel.append(milandyear['milage'])
                            model.append(cmodel)
                            caryear.append(milandyear['year'])
                            
        except:
            print 'error %d' %num
        num=num+100
        if num>2500:
            today=False
    ctime=mystrTime
    #print len(model)
    #print len(price)
    #print len(carlink)
    #print len(abstractInformation)
    #print len(mileagel)
    usercarlist=carlist(model,price,carlink,abstractInformation,mileagel,timePost,caryear)
    return usercarlist

def testcraglistsearch():
    usercarlist=craglistsearch('toyota','camry','2007','2010',5000,10000,'2015-03-06 23:40:13')   
    for i in range(len(usercarlist.modellist)):
        print usercarlist.modellist[i]
        print usercarlist.pricelist[i]
        print usercarlist.carlinklist[i]
        print usercarlist.abstractIlist[i]
        print usercarlist.timepostlist[i]
        print '--------------------------'
        
#testcraglistsearch()
#getMilageAndYear('http://raleigh.craigslist.org/cto/4902572544.html')
