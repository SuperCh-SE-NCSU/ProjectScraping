import os, sys
path = os.path.abspath(os.path.join('pythontemp_model'))
sys.path.append(path)

import unittest
import mock
from extractPricekbb_v0 import *

class Testkbb(unittest.TestCase):
	def setUp(self):
		self.year = '2007'
		self.make = 'Toyota'
		self.model = 'Corolla'

	def test_extractPricekbb(self):
		self.response = urllib2.urlopen("http://www.kbb.com/toyota/corolla/2007-toyota-corolla/ce-sedan-4d/?condition=very-good&vehicleid=84286&intent=buy-used&category=sedan&pricetype=private-party&mileage=30000&persistedcondition=very-good#survey")
		self.html = self.response.read()
		self.price = extractPricekbb(self.html)
		self.assertEqual(self.price, '9879')

	def test_kbbBaseUrl(self):
		self.baseUrl = kbbBaseUrl(self.make,self.model,self.year)
		self.assertEqual(self.baseUrl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla')

	#def kbbBaseUrl(self.make,self.model,self.year):
   	#	mk = make.lower().replace(' ', '-')
    #	md = model.lower().replace(' ', '-')
    #	yr = year.lower().replace(' ', '-')
    #	return "http://www.kbb.com/{make:}/{model:}/{year:}-{make:}-{model:}".format(self.make=mk,self.model=md,self.year=yr)

	#def test_kbbCarUrl(self):
	#	self.trim = 's-sedan-4d'
	#	#@mock.patch('extractPricekbb_v0.kbbCarUrl', side_effect=simple_kbbCarUrl)
	#	self.kbbcarurl = kbbCarUrl(self.make,self.model,self.year,self.trim)
    #	self.assertEqual(self.kbbcarurl, 'http://www.kbb.com/toyota/corolla/2007-toyota-corolla/s-sedan-4d?condition=good&intent=buy-used&pricetype=retail&persistedcondition=good')


if __name__ == '__main__':
    unittest.main()
