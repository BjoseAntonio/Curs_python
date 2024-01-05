print("____________Ejercicio 1___________________")
# Verificación de Número Par:
# Problema: Escribe un programa que solicite al usuario ingresar un número e indique si es par o impar.
# Pista: Utiliza el operador % para verificar si un número es divisible por 2.
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0 :
    print("Número par")
else:
    print("Número impar")



print("____________Ejercicio 2___________________")
# Calificación de Examen:
# Problema: Crea un programa que solicite al usuario ingresar su calificación en un examen (0-100) y muestre un mensaje de aprobación si la calificación es 60 o superior, de lo contrario, un mensaje de reprobación.
# Pista: Usa una estructura if para comparar la calificación.
califacion_Usuario = float(input("Ingrese la calificación: "))

if califacion_Usuario >= 60:
    print("¡Felicidades! Ha aprobado el examen.")
else:
    print("Lo siento, ha reprobado el examen.")



print("____________Ejercicio3___________________")
# Categoría de Edad:
# Problema: Escribe un programa que solicite al usuario ingresar su edad y muestre un mensaje indicando si es un niño (0-12 años), adolescente (13-19 años), adulto (20-59 años) o adulto mayor (60 años en adelante).
# Pista: Utiliza varias sentencias if y elif para evaluar diferentes rangos de edad.
edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 12:
    print("Eres un niño")

elif edad >= 13  and edad <= 19 :
    print("Es un adolecente ")

elif edad >= 20  and edad <= 59 :
    print("Es un adulto")

else:
    print("Es un adulto mayor ")



print("____________Ejercicio 4___________________")
# Comparación de Números:
# Problema: Crea un programa que solicite al usuario ingresar dos números y muestre un mensaje indicando cuál de los dos números es mayor, o si son iguales.
# Pista: Usa la sentencia if para comparar los números.
numero_x = float(input("Ingrese el primer número: "))
numero_y = float(input("Ingrese el segundo número: "))

if numero_x > numero_y:
    print("El primer número '",numero_x,"' es mayor que el segundo número '",numero_y,"'")
elif numero_y > numero_x:
    print("el segundo número '", numero_y,"' es mayor que el primer número '",numero_x,"'")
else:
    print("El primer número '",numero_x,"' es igual que el segundo número '",numero_y,"'")


print("____________Ejercicio 5___________________")
# Verificación de Número Positivo, Negativo o Cero:
# Problema: Escribe un programa que solicite al usuario ingresar un número e indique si es positivo, negativo o cero.
# Pista: Utiliza una combinación de if y else para manejar los diferentes casos.
verificacion_numero = float(input("Escribe un numero: "))

if verificacion_numero < 0:
    print("El número es NEGATIVO")

elif verificacion_numero == 0:
    print("El número es CERO")

else:
    print("El número es POSITIVO")