
dupla = (100,'Hola', [1,2,3],-50, 50,'Mundo')

#Para acceder al valor de la dupla
print(dupla)

#Acceder un valor especifico o limitante 
print(dupla[2])
print(dupla[1:4])

#Acceder a un valor dentro de la misma dupla en este caso a la lista
print(dupla[2][2])

#index para verificar valor existente
print(dupla.index('Hola'))
#print(dupla.index('Hol')) #Error 

#Cuantas veces esta el valor 
resultado = dupla.count(100)
print(resultado)