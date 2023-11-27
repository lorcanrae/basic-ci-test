# pylint: disable-all

import unittest
from package.helper import sum_of_a_and_b

class TestSample(unittest.TestCase):
    def test_sample(self):
        # We are simply checking whether 42==42!
        self.assertEqual(42, 42)

    def test_sum_of_a_and_b(self):

        res_ = sum_of_a_and_b(1, 1)
        self.assertIsInstance(res_, int)
