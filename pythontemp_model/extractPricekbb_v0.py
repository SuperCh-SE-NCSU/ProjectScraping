import requests,sys,csv,traceback,re,json,os,urllib2
from bs4 import BeautifulSoup
from random import random,shuffle
from time import sleep
global str

### Kelly Blue Book ######################

def extractPricekbb(html):
    price=re.search(r'"privatepartyexcellent": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price:
        return price.group(1)
    else:
        return 0
    
def kbbExtractJson(html):
    soup = BeautifulSoup(html, "lxml")
    jssearch = soup.find(name='script', attrs={'language' : 'javascript'})
    if jssearch:
        code = jssearch.text
    else:
        open("nojs.html", "w").write(html)
        raise RuntimeError

    js = code[code.find("data"):]
    js = js[js.find("{"):]
    bc = 0
    idx = 0
    for c in js:
        if bc == 0 and idx>0: break
        if c=="{": bc +=1
        if c=="}": bc -= 1
        idx+=1
    else:
        raise RuntimeError("bc={}".format(bc))

    jsonstr = js[:idx]

    return json.loads(jsonstr)


def kbbGetData(sess, make,model,year):
    kbbdata = dict()
    kbbCacheFile = "{}/{}-{}-{}_kbb.json".format(cacheDir,make,model,year)
    if os.path.isfile(kbbCacheFile):
        kbbdata = json.load(open(kbbCacheFile))
    else:
        kbbdata = getKbbData(sess, make,model,year)
        json.dump(kbbdata, open(kbbCacheFile, "w"))

    return kbbdata


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


def getKbbData(make,model,year):
    # 1.) get body types
    #html, session = getHtml(kbbBodytypeUrl(make,model,year),
    #                       cookies=dict(ZipCode=zipcode,PersistentZipCode=zipcode))
    response=urllib2.urlopen(kbbBodytypeUrl(make,model,year))
    html=response.read()
   
    re_bodystyle = re.compile(r'bodystyle=([^"\'?]+)')
    bodytypes = list(set(re_bodystyle.findall(html)))

    # 2.) get all trims
    trims = set()


    for b in bodytypes:
        print kbbTrimUrl(make,model,year,b)
        response=urllib2.urlopen(kbbTrimUrl(make,model,year,b))
        html=response.read()
        soup = BeautifulSoup(html, "lxml")

        vs = soup.find_all(text='Choose this style')
        for v in vs:
            href = v.parent.attrs['href']
            trims.add("http://www.kbb.com"+href)
    #print trims
    # 3.) scrape data for each trim
    scraped = dict()
    for t in trims:
        response=urllib2.urlopen(t)
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

            soup=BeautifulSoup(html2,"lxml")
            trims3=set()
            vs3=soup.find_all(text='Get used car price')

            for v3 in vs3:
                href=v3.parent.attrs['href']

                href=href.replace('retail', 'private-party')
                trims3.add("http://www.kbb.com"+href)

        #jd = kbbExtractJson(html)
        #scraped[t] = jd['values']
    print scraped
    return scraped

year='2007'
make='Toyota'
model='Corolla'
#pricing=getKbbData(make,model,year)

