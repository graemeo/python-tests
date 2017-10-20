import unittest
import demo

class DemoTest(unittest.TestCase):

    def test_should_add_up_numbers(self):
       # given 
       # when
       expected = demo.add_me_up(1, 1)

       # then
       self.assertEqual(expected, 2)

    def test_should_add_up_negative_numbers(self):
       # given
       # when
       expected = demo.add_me_up(-1, 2)

       # then
       assert expected == 1
