import unittest

def palindrome(palabra): 
    return palabra == palabra[::-1] 

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome("oso"))
        self.assertFalse(palindrome("detergente"))
        self.assertTrue(palindrome("ojo"))

        print("Tests ejecutados correctamente!")
        
if __name__ == '__main__':
    unittest.main()
