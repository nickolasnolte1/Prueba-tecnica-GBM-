def palindrome(palabra): 
    return palabra == palabra[::-1] 
print(palindrome("ana")) 
print(palindrome("carro")) 
print(palindrome("oso"))