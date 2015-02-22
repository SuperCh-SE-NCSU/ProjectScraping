import sys
import re
def extractPricekbb(html):
    price=re.search(r'"privatepartyexcellent": \{\s*"priceMin":\s*\d*\.\d*,\s*"price":\s*(\d*)\.\d*,\s*"priceMax":\s*\d*\.\d*\s*\}',html)
    if price:
        return price.group(1)
    else:
        return 0
#html=open('test.html').read()

#print extractPricekbb(html)
