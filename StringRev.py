import unittest
from will_string import reverse, cut, download
import string
import requests
import json

class UrlDownload(unittest.TestCase):
    def testDownload(self):
         ranNum = (random.randint(1,10)
         finNum = str(randNum)
         self.assertGreater(self, finNum)
         

class StringTests(unittest.TestCase):

     def testReverse(self):
          original = 'hello there'
          expected = original[::-1] 
          result = reverse(original)
          self.assertIsNotNone(result)
          self.assertEqual(expected, result)

     def testCut(self):
          input = 'testing'
         
          output = input[n]
          final = cut(output)
          self.assertEqual(output, final)
  
     def testOver18(self):
          age = 64
          takeAge = age - 18
          resultAge = Over18(takeAge)
          if resultAge():
                 
self.assertIsNot(takeAge, resultAge)

if __name__ == '__main__':
      unittest.main()
