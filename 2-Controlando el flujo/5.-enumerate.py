elementos = ['Hola', 4, 'Adíos', [1,2,3]]

for dupla in enumerate(elementos):
    print(dupla)


for indice, valor in enumerate(elementos):
    print(indice, valor)

lista_cadena =['Hola', 'Mundo']

for i,v in enumerate(lista_cadena):
    lista_cadena[i] = lista_cadena[i][0] 
    print(lista_cadena)