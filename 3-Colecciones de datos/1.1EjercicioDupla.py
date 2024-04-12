# A partir de una variable llamada tupla (la cuál no sabes qué contiene) debes imprimir por pantalla los siguientes apartados (usando un print() para cada apartado), de forma ordenada:

# El último elemento de la tupla.

# El número de elementos que tiene la tupla.

# La posición donde se encuentra el número 123 de la tupla.

# Una lista con los primeros tres elementos de la tupla.

# El elemento que hay en la posición con índice 4 de la tupla.

# El número de veces que aparece el número 4 en la tupla.
dupla = (2,4,5,6,123,'hola',4)

print(dupla[-1])
print(len(dupla))
# print()
print(dupla[0:3])
print(dupla[4])
print(dupla.count(4))