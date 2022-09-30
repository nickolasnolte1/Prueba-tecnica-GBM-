import unittest
from jumps import jumps

class Test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps(2750),19)
        self.assertEqual(jumps(1480),15)
        self.assertEqual(jumps(450),12)


if __name__ == "__main__":
    unittest.main()