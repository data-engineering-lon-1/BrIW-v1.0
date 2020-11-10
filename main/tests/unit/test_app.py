import unittest
from unittest.mock import patch, Mock
from main.src.models.functions.create_functions import print_dict


class Test_App(unittest.TestCase):

    @patch("builtins.print")
    def test_print_dict_function(self, mocker):
        dict_example = {1: "Tom", 2: "Boy"}
        print_dict(dict_example, "Test table")

        self.assertEqual(mocker.call_count, 5)

if __name__ == '__main__':
    unittest.main()
