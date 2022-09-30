G = int(input("> Ingrese el número de carreras: ")) #número de carreras
P = int(input("> Ingrese el número de pilotos en cada carrera: ")) #número de pilotos

# Resultados de cada carrera
resultados = []
for i in range(G):
    resultados.append([int(x) for x in input("\n> Ingrese los resultados de cada carrera: ").split()])

S = int(input("\n> Ingrese cuántos sistemas de puntaje hay: ")) #Cuántos sistemas de puntaje hay. 

print("(\nTomar en cuenta que el primero número que se introduzca, corresponde a la cantidad de pilotos que\n reciben puntos y el resto de datos corresponden a los puntos que recibe cada posición de la carrera.)")

# Lee los sistemas de puntaje
sistemas_puntaje = [] #inicializa una lista vacía.
for i in range(S): # itera a través de la cantidad de sistemas de puntuación (S), leyendo los datos de cada uno.
    K, puntos = [int(x) for x in input("\n> Ingrese uno de los sistemas de puntaje: ").split()[:2]] # toma los datos de entrada y los separa en dos listas: una con la cantidad de pilotos que reciben puntos (K) y otra con los puntos que recibe cada uno.
    sistemas_puntaje.append([K, puntos]) # agrega estas dos listas a la lista inicial.

# Calcular los puntos de los pilotos con cada sistema
for K, puntos in sistemas_puntaje:
    #inicializa los puntos de los pilotos en 0
    puntos_piloto = [0]*P
    
    #Agrega los puntos a los pilotos después de cada carrera.
    for race in resultados:
        for i in range(K):
            puntos_piloto[race[i]-1] = puntos[i] 
    
    #Busca la mayor cantidad de puntos acumulados
    max_puntos = max(puntos_piloto)
    
    #busca a qué piloto corresponden esos puntos
    max_pilotos = [i+1 for i in range(P) if puntos_piloto[i] == max_puntos]
    
    #Imprimir el/los pilotos con más puntos
    print(' '.join(str(x) for x in max_pilotos))
