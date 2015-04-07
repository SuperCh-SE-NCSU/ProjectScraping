from os.path import join as join
import re
import sys
import bs4
import json
import pickle
import os.path
import requests

KBB = "http://www.kbb.com"
COOKIES = {'ZipCode': '27606'}

class PageNotFoundError(StandardError):
    def __init__(self, page):
        super(PageNotFoundError, self).__init__()
        self.page = page

# Get a list of all car manufacturers from KBB using the /new-cars/ page.
def fetch_all_makes():
    print(join(KBB, "used-cars"))
    html = fetch(join(KBB, "used-cars"), cookies=COOKIES)
    
    # Find all <a> tags.
    makes = []
    for link in html.find_all("a",
            href=re.compile("\?vehicleclass=usedcar&intent=buy-used")):
        makes.append(str(link.contents[0]))

    # Filter out newlines
    makes = filter(lambda x: x != '\n', makes)

    # Filter out duplicates
    makes = list(set(makes))
    return makes

# Make 'word' safe to put in a URL
def urlize_word(word):
    return word.strip().replace(' ', '-').lower()

# Utility functions
def fetch(url, cookies=None):
    print('fetching: {}'.format(url))
    resp = requests.get(url, cookies=cookies)
    html = bs4.BeautifulSoup(resp.content)
    if html.find_all(re.compile('page not found', re.IGNORECASE)):
        raise PageNotFoundError
    return html

#print(fetch(join(KBB, 'scion')))
#sys.exit(1)

cars = []

try:
    # Simple caching client-side of cars/models
    for maker in fetch_all_makes():
        makename='model/'+maker+'.json'
        cars=[]
        if os.path.exists(makename):
            with open(makename, 'r') as c:
                cars = json.loads(c.read())
        else:
            maker_url = join(KBB, urlize_word(maker))
            html = fetch(maker_url, cookies=COOKIES)
            for model in html.find_all('a', class_='section-title'):
                cars.append({
                    'model': model.contents[0],
                    'modelurl': join(KBB,model['href'])
                })
            with open(makename, 'w') as c:
                c.write(json.dumps(cars, indent=4, sort_keys=True))
except PageNotFoundError as perror:
    print("[error]: page '{}' not be found".format(perror.page))
    sys.exit(1)
