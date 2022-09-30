import unittest
from jumps import jumps

class Test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps(5),4)
        self.assertEqual(jumps(82),9)
        self.assertEqual(jumps(27),7) #En este caso, este assert erramos el resultado a propósito para ver que el test si funcione bien. 


if __name__ == "__main__":
    unittest.main()