# numeros = [1,2,3,4,5,6,7,9,10]

# indice = 0 

# for numero in numeros:
#     print(numero)

# #Para modificar la lista es necesario tomar la lista
# for numero in numeros:
#     numeros[indice] *=10
#     indice += 1
# print(numeros)


# #Otra manera de crear un indice es directo desde el For

# for i, num in enumerate(numeros):
#     numeros[i] *=100
# print(numeros)

#Letras 
cadena = 'Hola mundo'
cadena2 = ''

for caracter in cadena:
    print(caracter)

for caracter in enumerate(cadena):
    cadena2 += '*'

