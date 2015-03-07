import requests,sys,csv,traceback,re,json,os,urllib2
from bs4 import BeautifulSoup
from random import random,shuffle
from time import sleep
import modelCragList_v1_debug
global str


### Kelly Blue Book ######################

def extractPricekbb(html):
    pricelist=list()
    price1=re.search(r'"privatepartyexcellent": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price1:
        pricelist.append(price1.group(1))
    else:
        pricelist.append(0)
        
    price2=re.search(r'"privatepartyverygood": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price2:
        pricelist.append(price2.group(1))
    else:
        pricelist.append(0)
        
    price3=re.search(r'"privatepartygood": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price3:
        pricelist.append(price3.group(1))
    else:
        pricelist.append(0)

    price4=re.search(r'"privatepartyfair": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price4:
        pricelist.append(price4.group(1))
    else:
        pricelist.append(0)

    price5=re.search(r'"privatepartyfair": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price5:
        pricelist.append(price5.group(1))
    else:
        pricelist.append(0)

    price6=re.search(r'"retail": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price6:
        pricelist.append(price6.group(1))
    else:
        pricelist.append(0)
    
    return pricelist


def kbbBaseUrl(make,model,year):
    mk = make.lower().replace(' ', '-')
    md = model.lower().replace(' ', '-')
    yr = year.lower().replace(' ', '-')
    return "http://www.kbb.com/{make:}/{model:}/{year:}-{make:}-{model:}".format(make=mk,model=md,year=yr)


def kbbCarUrl(make,model,year,trim):
    b = kbbBaseUrl(make,model,year)
    return b + "/{}?condition=good&intent=buy-used&pricetype=retail&persistedcondition=good".format(trim)


def kbbBodytypeUrl(make,model,year):
    b = kbbBaseUrl(make,model,year)
    return b + "/categories/?intent=buy-used"


def kbbTrimUrl(make,model,year, body):
    b = kbbBaseUrl(make,model,year)
    return b + "/styles/?intent=buy-used&bodystyle={}".format(body)

def savehtml(filedst,content):
    Html_file= open(filedst,"w")
    Html_file.write(content)
    Html_file.close()

def getKbbPrice(make,model,year,mileage):
    #get make model year
    response=urllib2.urlopen(kbbBodytypeUrl(make,model,year))
    html=response.read()
    #get style like sedan
    re_bodystyle = re.compile(r'bodystyle=([^"\'?]+)')
    bodytypes = list(set(re_bodystyle.findall(html)))
    trims = dict()
    styleprice=dict()
    
    for b in bodytypes:
        #print kbbTrimUrl(make,model,year,b)
        response=urllib2.urlopen(kbbTrimUrl(make,model,year,b))
        html=response.read()
        soup = BeautifulSoup(html, "lxml")

        #get style in the second level like CE/LE
        vs = soup.find_all(text='Choose this style')
        #http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
        for v in vs:
            #print v.parent
            style=v.parent.parent.find_all("div",{"class":"style-name section-title"})[0].get_text()
            #print style
            href = v.parent.attrs['href']
            trims[style]="http://www.kbb.com"+href

    #print trims
    for key1,value1 in trims.iteritems():
        #html, session = getHtml(kbbCarUrl(make,model,year,t), session)
        #print t+'&pricetype=private-party&persistedcondition=good'
        response=urllib2.urlopen(value1)
        html=response.read()
        soup=BeautifulSoup(html,"lxml")
        trims2=set()
        vs2=soup.find_all(text='Choose price type')
        for v in vs2:
            href=v.parent.attrs['href']
            trims2.add("http://www.kbb.com"+href)
        
        for t2 in trims2:
            response2=urllib2.urlopen(t2+'&pricetype=private-patry')
            html2=response2.read()
            #print html2

            soup=BeautifulSoup(html2,"lxml")
            trims3=set()
            vs3=soup.find_all("a",{"data-condition-select":"verygood"},text='Get used car price')
            #print vs3
            for v3 in vs3:
                href=v3.attrs['href']
                href=href.replace('retail', 'private-party')
                response=urllib2.urlopen("http://www.kbb.com"+href+'&mileage='+str(mileage))
                html3=response.read()
                styleprice[key1.replace('\n', ' ').replace('\r', '')]=extractPricekbb(html3)
                trims3.add("http://www.kbb.com"+href)
            #print trims3
        #print html
        #jd = kbbExtractJson(html)
        #scraped[t] = jd['values']
    print styleprice
    return styleprice
    #print kbbBodytypeUrl(make,model,year)
    #savehtml("test.html",html)
        
class carlistwithPrice:
    def __init__(self,standardpricelist,modellist,pricelist,carlinklist,abstractIlist,timepostlist):
        self.modellist=modellist
        self.standardpricelist=standardpricelist
        self.carlinklist=carlinklist
        self.abstractIlist=abstractIlist
        self.timepostlist=timepostlist
        self.pricelist=pricelist

def craglistsearchKbb(mcarlist):
    price=list()
    for i in range(len(mcarlist.modellist)):
        tempprice=getKbbPrice(mcarlist.make[i],mcarlist.model[i],mcarlist.year[i],mcarlist.mileage[i])
        price.append(tempprice)
        
def testgetKbbPrice():
    getKbbPrice('Honda','Accord','2007',111000)
testgetKbbPrice()
