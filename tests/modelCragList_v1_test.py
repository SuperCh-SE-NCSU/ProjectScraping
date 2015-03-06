#add file(pythontemp_model) to PYTHONPATH in order to import being-tested file
import os, sys
path = os.path.abspath(os.path.join('pythontemp_model'))
sys.path.append(path)

import unittest
from modelCragList_v1_debug import getMilageAndYear

class Testcraigslist(unittest.TestCase):
	def setUp(self):
		self.milageandy = getMilageAndYear('http://raleigh.craigslist.org/cto/4902572544.html')   
		
	#consider indention carefully   
	def test_getMilageAndYear(self):
		self.assertEqual(self.milageandy, {'milage': '106000','year': '2006'})
       
if __name__ == '__main__':
    unittest.main()
