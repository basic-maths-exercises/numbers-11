import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_isRational(self) :
        self.assertTrue( isRational(1,0)==0, "your function is not working" )
        for i in range(200) :
             a, b = np.random.randint(-10,10), np.random.randint(-10,10)
             if b==0 : self.assertTrue( isRational(a,b)==0, "your function is not working" )
             else : self.assertTrue( isRational(a,b)==1, "your function is not working" )
