import unittest
from jumps import jumps

class Test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps(0),0)
        self.assertEqual(jumps(1),1)
        self.assertEqual(jumps(138),10)


if __name__ == "__main__":
    unittest.main()