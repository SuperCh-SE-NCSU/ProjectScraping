#add file(pythontemp_model) to PYTHONPATH in order to import being-tested file
import os, sys
path = os.path.abspath(os.path.join('bin'))
sys.path.append(path)

import unittest
from modelCragList_v2_debug import *

class Testcraigslist(unittest.TestCase):
	def setUp(self):
		pass		
		
	#consider indention carefully 
	def test_getMilageAndYear(self):
		self.milageandy = getMilageAndYear('http://raleigh.craigslist.org/cto/4902572544.html')
		self.assertEqual(self.milageandy, {'milage': '106000','year': '2006'})
           
	def test_craglistsearch(self):
		self.usercarlist=craglistsearch('toyota','camry','2007','2010',5000,10000,'2015-04-05 18:00:00')  
		self.assertIsNotNone(self.usercarlist)
		self.assertIsInstance(self.usercarlist, carlist)
		self.assertEqual(self.usercarlist.modellist[0],'camry')
		#assertGreaterEqual(a, b)  a>=b
		self.assertGreaterEqual(int(self.usercarlist.pricelist[0]),5000)
		self.assertLessEqual(int(self.usercarlist.pricelist[0]),10000)


             
if __name__ == '__main__':
	unittest.main()
