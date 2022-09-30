import unittest
import jumps

class Test(unittest.TestCase):
    def test_jumps_1(self):
        x = 4
        result = 3
        self.assertEqual(jumps(x), result)

    def test_jumps_2(self):
        x = 5
        result = 4
        self.assertEqual(jumps(x), result)

    def test_jumps_3(self):
        x = 6
        result = 4
        self.assertEqual(jumps(x), result)

    def test_jumps_4(self):
        x = 7
        result = 5
        self.assertEqual(jumps(x), result)

if __name__ == "__main__":
    unittest.main()