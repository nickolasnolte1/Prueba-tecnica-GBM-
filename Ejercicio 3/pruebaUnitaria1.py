import unittest
import jumps
 
class TestMinJumps(unittest.TestCase):
    def test_case_1(self):
        x = 6
        expected = 2
        result = minJumps(x)
        self.assertEqual(expected, result)
 
    def test_case_2(self):
        x = 10
        expected = 3
        result = minJumps(x)
        self.assertEqual(expected, result)
 
    def test_case_3(self):
        x = 15
        expected = 4
        result = minJumps(x)
        self.assertEqual(expected, result)
 
if __name__ == '__main__':
    unittest.main()