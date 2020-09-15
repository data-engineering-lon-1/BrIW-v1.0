import unittest
from unittest.mock import patch

class Test_RW_functions(unittest.TestCase):
    @patch('BriW.functions.read_write_functions.csv_reader')
    def test_csv_writer(self, mock_csv_reader):
        with open(csv_file, "r") as r:
            reader = csv.reader(r)
            
            for row in reader:
                person = row[0]
                drink = row[1]
                dict_file[person] = drink