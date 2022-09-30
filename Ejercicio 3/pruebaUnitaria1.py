import unittest
from jumps import jumps

class Test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps(13),6)
        self.assertEqual(jumps(98),9)
        self.assertEqual(jumps(31),9)

if __name__ == "__main__":
    unittest.main()