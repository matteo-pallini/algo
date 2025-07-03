import unittest

from strings.rabin_karp_algo import rabin_karp


class TestRabinKarp(unittest.TestCase):

    def test_base_case(self):
        main_text = "We all love the wild red tailed fox"
        target_string = "wild"
        actual = rabin_karp(main_text, target_string, 256, 101)
        expected = 16
        self.assertEqual(expected, actual)

    def test_that_only_first_instance_get_matched(self):
        main_text = "We all love wildly the wild red tailed fox"
        target_string = "wild"
        actual = rabin_karp(main_text, target_string, 256, 101)
        expected = 12
        self.assertEqual(expected, actual)

    def test_no_match(self):
        main_text = "We all love the red tailed fox"
        target_string = "wild"
        actual = rabin_karp(main_text, target_string, 256, 101)
        expected = None
        self.assertEqual(expected, actual)