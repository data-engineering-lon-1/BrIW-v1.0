import unittest
from unittest.mock import patch, Mock

class Test_App(unittest.TestCase):

    @patch("builtins.print")
    def test_print_function(self, mocker):
        # mock_item = Mock(Person)

        print("example of something to print")
        print("example of something else to print")

        self.assertEqual(mocker.call_count, 2)

