import unittest
from will_string import reverse, cut, Over18
import string

class StringTests(unittest.TestCase):

     def testReverse(self):
          original = 'hello there'
          expected = original[::-1] 
          result = reverse(original)
          self.assertIsNotNone(result)
          self.assertEqual(expected, result)

     def testCut(self):
          input = 'testing'
          output = input[:4]
          final = cut(output)
          self.assertEqual(output, final)
  
     def testOver18(self):
          age = 64
          takeAge = age - 18
          resultAge = Over18(takeAge)
          self.assertIsNot(takeAge, resultAge)

if __name__ == '__main__':
      unittest.main()
