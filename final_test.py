import unittest
import final 
from math import pi 
import numpy as np
import random
import sys  

class Test_getFilePath(unittest.TestCase):
    def test_algo(test):
        grupos = 4
        grupo = int(grupos)
        test.assertAlmostEqual(final.getFileData("C:\\Users\\Miguel\\Downloads\\Group-Code-master\\file1.txt"), 12)
        
    def test_algo2(test):
        test.assertAlmostEqual(final.getFileData("C:\\Users\\Miguel\\Downloads\\Group-Code-master\\file2.txt"),8)   

class Test_randomnizeData(unittest.TestCase):
    def test_uno(test):
         array = []
         array = final.randomizeData(12,"C:\\Users\\Miguel\\Downloads\\Group-Code-master\\file1.txt"  )
         count = 0
         
         for i in range(1000000):
            
             if(final.randomizeData(12,"C:\\Users\\Miguel\\Downloads\\Group-Code-master\\file1.txt"  ) == array):
                 count = count + 1
         if(count >= 100000):
             test.defaultTestResult
            

             

   