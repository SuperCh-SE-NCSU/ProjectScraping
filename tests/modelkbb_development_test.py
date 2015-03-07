import os, sys
path = os.path.abspath(os.path.join('pythontemp_model'))
sys.path.append(path)

import unittest
from extractPricekbb_v0 import *

class Testkbb(unittest.TestCase):
	def setUp(self):
		pass

	def test_extractPricekbb(self):
		self.response = urllib2.urlopen("http://www.kbb.com/toyota/corolla/2007-toyota-corolla/ce-sedan-4d/?condition=very-good&vehicleid=84286&intent=buy-used&category=sedan&pricetype=private-party&mileage=30000&persistedcondition=very-good#survey")
		self.html = self.response.read()
		self.price = extractPricekbb(self.html)
		self.assertEqual(self.price, '9879')


if __name__ == '__main__':
    unittest.main()
