#Ejercicio numero 1
numeroX = float(input("Escriba un numero x:"))
numeroY = float(input("Escriba un segundo y: "))
print("Los dos número son iguales:",numeroX == numeroY)
print("Los dos número son diferentes:",numeroX != numeroX)
print("El primer número es mayor que el segundo:",numeroX > numeroY)
print("El segundo es mayor o igual que el primero:",numeroX <= numeroY)

#Ejercicio número 2
#2) Utilizando operadores lógicos, determinar si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10
texto = input("Introduce un texto: ")

print("El texto tiene un longitud mayor o igual que 3 y a su vez menor que 10",len(texto) >= 3 and len(texto) < 10)

#Ejercicio 3
#Realizar un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
#Guardar en una variable numero_magico el valor 12345679(sin el 8)
#Lee por pantalla otro numero_usuario especifica que sea entre 1 y 9 (asegúrate que es número)
#Multiplica numero_usuario por 9 en si mismo
# Multiplica el numero_magico por el numero_usuario en si mismo 
# Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
numero_usuario = int(input("Ingrese un número entre 1 y 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print(numero_magico) 
