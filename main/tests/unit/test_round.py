import unittest
from main.src.models.classesforapp.round import Round, Person, Drink
from unittest.mock import patch

class Test_Classes(unittest.TestCase):
    def test_person(self):

        expected = "Sarah"

        actual = Person("Sarah").firstName

        self.assertEqual(expected, actual)

    def test_drink(self):

        expected = "Beer"

        actual = Drink("Beer").drink

        self.assertEqual(expected, actual)
    

if __name__ == "__main__":
    unittest.main()
