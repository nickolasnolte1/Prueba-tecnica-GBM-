G = int(input("Ingrese el número de Grand Prix: ")) # número de GP
P = int(input("Ingrese el número de pilotos: ")) # numero de pilotos

#Crea un diccionario vacío para guardar los puntos de cada piloto
points = {}
for i in range(1, P+1):
    points[i] = 0


#Para cada GP, agregar los puntos de cada piloto al diccionario
for i in range(G):
    order = input().split()
    for j in range(P):
        points[j+1] += int(order[j])

#Encontrar el número máximo de puntos
max_points = 0
for i in range(1, P+1):
    if points[i] > max_points:
        max_points = points[i]

#Imprimir la lista de pilotos con el mayor número de puntos
for i in range(1, P+1):
    if points[i] == max_points:
        print(i, end=" ")