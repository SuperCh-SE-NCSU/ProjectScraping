import urllib2
f=urllib2.urlopen('http://raleigh.craigslist.org/search/cto//')
print f
print f.read()
