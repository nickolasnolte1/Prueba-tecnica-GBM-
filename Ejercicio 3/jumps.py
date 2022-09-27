t = int(input("Ingrese el número de test cases: ")) # El número de test cases
for i in range(t):
    x = int(input("Ingrese el punto de destino: ")) # El punto de destino
    jumps = 0 # El contador de saltos, comienza en cero
    while x > 0: # mientras no hayamos llegado al punto deseado...
        if x % 2 == 0: # si X es par 
            x = x / 2 # we can jump to x/2 -- x is divided by 2 because if x is even, the minimum number of jumps to reach x is x / 2.
        else: # si X es impar
            x = x - 1 # we can jump to x-1 -- The idea is that if x is even, we can divide it by 2 in one jump, and if x is odd, we can subtract 1 from it in one jump. So the minimum number of jumps to reach x is the number of times we have to divide x by 2 or subtract 1 from it.
        jumps += 1 # agregar un salto al contador
    print("El número mínimo de saltos es: ")
    print(jumps) # imprimir el número mínimo de saltos

