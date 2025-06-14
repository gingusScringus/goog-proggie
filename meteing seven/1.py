import unittest
import os

def add(a, b):
    value = a+b
    return value

def sayN():
    return "Nintendo"

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_nonequal(self):
        self.assertNotEqual(add(2, 3), 7)
    def test_greater(self):
        self.assertGreater(add(5, 3), 7)
    def test_less(self):
        self.assertLess(add(2, 3), 10)

class TestSayNFunction(unittest.TestCase):
    def test_sayN(self):
        self.assertEqual(sayN(), "Nintendo")

if __name__ == '__main__':
    os.system("cls" if os.name == "nt" else "clear")

    unittest.main()