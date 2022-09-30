import unittest

def jumps(x):
    jumps = 0 # El contador de saltos, comienza en cero
    while x > 0: # continuar iterando mientras no hayamos llegado al punto deseado
        if x % 2 == 0: # si X es par 
            x = x / 2
        else: # si X es impar
            x = x - 1
        jumps += 1 # agregar un salto al contador
    return jumps

t = int(input("\nIngrese el número de test cases: ")) # El número de test cases
for i in range(t):
    x = int(input("\nIngrese el punto de destino: ")) # El punto de destino
    print("El número mínimo de saltos es: ", jumps(x)) # imprimir el número mínimo de saltos

