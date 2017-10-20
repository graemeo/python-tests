import unittest
from mock import mock
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

   def setUp(self):
      self.calculator = Calculator()

   def test_should_add_up_accurately_for_given_set_of_numbers(self):
      # given
      number_one = 1
      number_two = 2

      # when
      actual = self.calculator.add_me_up(number_one, number_two)

      # then
      self.assertEqual(3, actual)

   def test_should_add_up_accurately_for_negative_numbers(self):
      # given
      number_one = 1
      number_two = -2
     
      # when
      actual = self.calculator.add_me_up(number_one, number_two)

      # then
      assert actual == -1

   @unittest.skip("Skipper!")
   def test_this_is_not_real(self):
      # given
      # when
      # then
      assert 1 == 2
