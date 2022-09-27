def palindrome(palabra): 
    return palabra == palabra[::-1] 
print(palindrome("radar")) 
print(palindrome("carro")) 
print(palindrome("arenera"))