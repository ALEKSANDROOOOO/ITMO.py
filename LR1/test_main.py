import unittest
from main import two_sum


class TestTwoSum(unittest.TestCase):
  
  def test_nonetype(self):
    self.assertEqual(two_sum(None, 1), 'Список является NoneType')
  
  def test_notlist(self):
    self.assertEqual(two_sum(2, 1), 'На вход подан не список')
    



















