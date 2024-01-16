lista = ['Hola', 10, 'Adiós', [50, 19, 33]]

# print(lista[-1])

for i in lista[-1]:
    print(i)

lista2 = [
        'Hola', #Cadena
        (1,2,3,4,), #Dupla
        ['Azul', 'rojo', 'Amarillo']
]

# for coleccion in lista2:
#     for elemento in coleccion:
#         print(coleccion," --> ",elemento)

for indice_coleccion, coleccion in enumerate(lista2):
    for indice_elemento, elemento in enumerate(coleccion):
        # print(coleccion, elemento)
        print(lista2[indice_coleccion][indice_elemento])


tabla = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

for fila in tabla:
    for columna in fila:
        print(columna, end=" ")
    print()