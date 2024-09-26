
import unittest
import pytest 

class math_test1(unittest.TestCase):

    def _add(self, x, y):
        result = x+y
        self.assertEqual(result, 10, "It should be 10")

    
    #if __name__ == 

obj = math_test1()
obj._add(6,6)

print('Name : ',__name__)

class _mult(unittest.TestCase):

    def test_add(self):
        result = 5*2
        self.assertEqual(result, 10, "It should be 10")

    
   
if __name__ == '__main__':
    print('In')
    unittest.main()


