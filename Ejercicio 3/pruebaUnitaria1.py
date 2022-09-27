import unittest
import jumps 

class TestJumpToX(unittest.TestCase):
    def test_jump_to_x(self):
        self.assertEqual(jump_to_x(10), 3)

if __name__ == '__main__':
    unittest.main()