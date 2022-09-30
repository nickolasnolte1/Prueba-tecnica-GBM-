import unittest
from jumps import jumps

class Test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps(200),10)
        self.assertEqual(jumps(400),11)
        self.assertEqual(jumps(600),13)


if __name__ == "__main__":
    unittest.main()