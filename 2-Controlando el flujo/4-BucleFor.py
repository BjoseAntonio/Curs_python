numeros = [1,2,3,4,5,6,7,9,10]

indice = 0 

for numero in numeros:
    print(numero)

#Para modificar la lista es necesario tomar la lista
for numero in numeros:
    numeros[indice] *=10
    indice += 1
print(numeros)