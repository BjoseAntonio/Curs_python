# Bucles anidados
# En este ejercicio se te va a facilitar una variable matriz repleta de números enteros y de la cuál lo único que sabes es que contiene dos dimensiones.

# Aquí tienes una estructura de ejemplo ilustrando como se forma (lista con sublistas), muy parecida a una tabla:

matriz = [
    [8, 7, 0],
    [34, 2, -1],
    [5, -5, 12]
]

for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1
        print(matriz[i][j], end=' ')
    print()