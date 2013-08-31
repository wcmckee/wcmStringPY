import unittest
from will_string import reverse

class StringTests(unittest.TestCase):

     def testReverse(self):
          original = 'hello there'
          expected = original[::-1] 
          result = reverse(original)
          self.assertIsNotNone(result)
          self.assertEqual(expected, result)
if __name__ == '__main__':
      unittest.main()
