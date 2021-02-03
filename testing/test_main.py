try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_isRational(self) :
        inputs, outputs = [(1,0,)], [0]
        for i in range(200) :
             a, b = np.random.randint(-10,10), np.random.randint(-10,10)
             inputs.append((a,b,))
             if b==0 : outputs.append(0) 
             else : outputs.append(1)
        assert( fc.check_func( 'isRational', inputs, outputs ) )
