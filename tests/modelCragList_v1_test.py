#add file(pythontemp_model) to PYTHONPATH in order to import being-tested file
import os, sys
path = os.path.abspath(os.path.join('pythontemp_model'))
sys.path.append(path)

import unittest
from modelCragList_v1_debug import *

class Testcraigslist(unittest.TestCase):
	def setUp(self):
		pass		
		
	#consider indention carefully 
	def test_getMilageAndYear(self):
		self.milageandy = getMilageAndYear('http://raleigh.craigslist.org/cto/4902572544.html')
		self.assertEqual(self.milageandy, {'milage': '106000','year': '2006'})
           
	def test_craglistsearch(self):
		self.usercarlist=craglistsearch('toyota','camry','2007','2010',5000,10000,'2015-02-21 23:40:13')  
		self.assertIsNotNone(self.usercarlist)
		self.assertIsInstance(self.usercarlist, carlist)
		#self.assertEqual(self.usercarlist, <__main__.carlist instance at 0x7fb9a6b9c4d0>)
             
if __name__ == '__main__':
    unittest.main()
