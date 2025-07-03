import unittest
from mixed.sandbox import Solution

class MainTest(unittest.TestCase):
    sol = Solution()
    def test_main(self):
        s = "asdf"
        s = "nrqqigtqph"
        out = self.sol.run(s)
        self.assertEqual(out, 6)