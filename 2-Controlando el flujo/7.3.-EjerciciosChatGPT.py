# Ejercicio 1: Tabla de multiplicar
# Imprime la tabla de multiplicar del 1 al 10 usando bucles anidados.

for i in range(1,10):
    for j in range(1,10):
        print(i,' X ',j," = ",(i*j))
    print( )

# Ejercicio 2: Patrón de asteriscos
# Imprime un patrón de asteriscos en forma de triángulo.

f = 5
for i in range(1, f+1):
    for j in range(i):
        print('*', end=" ")
    print( )

# Ejercicio 3: Suma de matriz
# Dadas dos matrices, realiza la suma de ellas.

matriz1 = [ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz2 = [
    [9,8,7],
    [6,6,4],
    [3,2,1]
]

resultado = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]
print(resultado)



# Ejercicio 4: Pirámide invertida
# Imprime una pirámide invertida de números.
piramide = 5

for q in range(piramide, 0, -1):
    for w in range(piramide - q):
        print(" ", end=' ')
    for k in range(2 * q - 1):
        print(i, end=' ')
    print()

# Ejercicio 5: Tablero de ajedrez
# Imprime un tablero de ajedrez utilizando caracteres 'X' y 'O'.

tabla = 8
indice1 = 8

for indice in range(tabla):
    for columna in range(indice1):
        if (indice + columna) % 2 == 0:
            print("x", end=" ")
        else: 
            print("O", end=" ")
    print()