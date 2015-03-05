#add file(pythontemp_model) to PYTHONPATH in order to import being-tested file
import os, sys
path = os.path.abspath(os.path.join('pythontemp_model'))
sys.path.append(path)

print path
print sys.path

import modelCragList_v1_debug
import unittest
class Testcraigslist(unittest.TestCase):
    def setUp(self):
        self._init_()
        
if __name__ == '__main__':
    unittest.main()
