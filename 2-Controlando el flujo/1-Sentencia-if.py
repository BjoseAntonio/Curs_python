#permite dividir el flujo de un programa en diferentes caminos

a = 5
if a == 2:
    print("'a' vale 2")
if a == 5:
    print("'a' vale 5")

#if dentro otro if 
q = 4
r = 3

if q == 4:
    print("Q vale 4")
    if r == 3:
        print("R vale 3")

#Utilizando operador logico en if
numeroX = 7
numeroY =5

if numeroX == 7 and numeroY == 5:
    print("numeroX vale 7 y numeroY vale 5")


#Saber si el numero es par o no con "if y else"
b = 11
if b % 2 == 0:
    print("El número "+str(b)+" es par")
else:
    print("El número "+str(b)+" es impar")


#Utilizando if elif  y else
comando = "Salir"
if comando == "Entrar":
    print("Bienvenidos al acceso de RedMy")
elif comando == "Registrarse":
    print("Es necesario completar los datos")
elif comando == "Salir":
    print("Saliendo de RedMy...")
else:
    print("No se reconoce el comando introduccido")


#Utilizando un valor de entra por el usuario
nombreAlumno = input("Nombre  de Alumno: ")
calificacion = float(input("Asigne la calificación para el alumno "+nombreAlumno+" :"))

if calificacion >= 9:
    print("Sobresaliente")
elif  calificacion >= 7:
    print("Notable")
elif calificacion >= 6:
    print("Bien")
elif  calificacion >= 5:
    "Suficiente"
else:
    print("Insuficiente")


