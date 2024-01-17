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
    [6,5,4],
    [3,2,1]
]

resultado = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

