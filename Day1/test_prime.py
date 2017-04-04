import prime
import unittest

class test_prime (unittest.TestCase):
    def test_two(self):
        results = prime.prime_number(2)
        self.assertEqual([2], results)
    def test_eight(self):
        results = prime.prime_number(8)
        self.assertEqual([2, 3, 5, 7], results)
    def test_negative(self):
        results = prime.prime_number(-5)
        self.assertEqual([], results)
    def test_zero(self):
        results = prime.prime_number(0)
        self.assertEqual([], results)
    def test_data_type(self):
        results = prime.prime_number("hello")
        self.assertEqual("invalid data", results)
unittest.main()
    