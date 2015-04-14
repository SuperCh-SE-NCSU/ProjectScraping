import os, sys
from coveralls import Coveralls
path = os.path.abspath(os.path.join('bin'))
sys.path.append(path)

import unittest
from modelkbb_v1_debug import *

class Testkbb(unittest.TestCase):
	def setUp(self):
		self.year = '2007'
		self.make = 'Toyota'
		self.model = 'Corolla'
		self.mileage = '111000'

	def test_extractPricekbb(self):
		self.response = urllib2.urlopen("http://www.kbb.com/toyota/corolla/2007-toyota-corolla/ce-sedan-4d/?condition=very-good&vehicleid=84286&intent=buy-used&category=sedan&pricetype=private-party&mileage=30000&persistedcondition=very-good#survey")
		self.html = self.response.read()
		self.price = extractPricekbb(self.html)
		self.assertEqual(self.price, ['7616', '8000', '8384', '8857', '10209'])

	def test_kbbBaseUrl(self):
		self.baseUrl = kbbBaseUrl(self.make,self.model,self.year)
		self.assertEqual(self.baseUrl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla')

	def test_kbbCarUrl(self):
		self.trim = 's-sedan-4d'
		self.kbbcarurl = kbbCarUrl(self.make,self.model,self.year,self.trim)
		self.assertEqual(self.kbbcarurl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla/s-sedan-4d?condition=good&intent=buy-used&pricetype=retail&persistedcondition=good')

	#consider indention instead of whitespaces
	def test_kbbBodytypeUrl(self):
		self.kbbBodytypeUrl = kbbBodytypeUrl(self.make,self.model,self.year)
		self.assertEqual(self.kbbBodytypeUrl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla/categories/?intent=buy-used')

	def test_kbbTrimUrl(self):
		self.body = 'sedan'
		self.kbbTrimUrl = kbbTrimUrl(self.make,self.model,self.year,self.body)
		self.assertEqual(self.kbbTrimUrl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla/styles/?intent=buy-used&bodystyle=sedan')
		
	def test_getKbbPrice(self):
		self.kbbPrice = getKbbPrice(self.make,self.model,self.year,self.mileage)
		self.assertIsNotNone(self.kbbPrice)
		self.assertEqual(type(self.kbbPrice).__name__, 'dict')

if __name__ == '__main__':
	unittest.main()
