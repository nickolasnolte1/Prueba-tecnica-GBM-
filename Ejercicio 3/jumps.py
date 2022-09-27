t = int(input("Ingrese el número de test cases: ")) # El número de test cases
for i in range(t):
    x = int(input("Ingrese el punto de destino: ")) # El punto de destino
    jumps = 0 # El contador de saltos, comienza en cero
    while x > 0: # mientras no hayamos llegado al punto deseado...
        if x % 2 == 0: # si X es par 
            x = x / 2 
        else: # si X es impar
            x = x - 1
        jumps += 1 # agregar un salto al contador
    print("El número mínimo de saltos es: ")
    print(jumps) # imprimir el número mínimo de saltos


