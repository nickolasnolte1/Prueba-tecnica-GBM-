import unittest

def palindrome(palabra): 
    return palabra == palabra[::-1] 
print(palindrome("")) 
print(palindrome("")) 
print(palindrome(""))



class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertFalse(palindrome("carretera"))
        self.assertFalse(palindrome("lapicero"))
        self.assertTrue(palindrome("solos"))

        print("Tests ejecutados correctamente!")
        
if __name__ == '__main__':
    unittest.main()
