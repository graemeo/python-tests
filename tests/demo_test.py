import unittest
from mock import patch
import demo
from calculator import Calculator


class DemoTest(unittest.TestCase):

    @patch('demo.Calculator')
    def test_should_invoke_add_me_up_from_calculator(self, mocked_calculator):
       # given
       # when
       demo.calculate()

       # then
       mocked_calculator.return_value.add_me_up.assert_called_once()
