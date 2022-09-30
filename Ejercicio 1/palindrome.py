'''
La siguiente función verifica si una palabra el palíndroma o no (Verdadero si lo es, Falso si no es.)
'''

def palindrome(palabra): 
    return palabra == palabra[::-1]
print(palindrome("radar")) 
print(palindrome("carro")) 
print(palindrome("arenera"))



# Más palabras palíndromas para probar:
# oso
# ese
# ojo
# ana
# somos
# solos
# salas
# sometemos
# sagas
# seres