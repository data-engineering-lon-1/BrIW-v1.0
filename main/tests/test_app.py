import unittest
from unittest.mock import patch, Mock

from main.src.models.person import Person, print_person

class Test_App(unittest.TestCase):

    @patch("builtins.print")
    def test_print_function(self, mocker):
        # mock_item = Mock(Person)

        print("example of something to print")
        print("example of something else to print")

        self.assertEqual(mocker.call_count, 2)