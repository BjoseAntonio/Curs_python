print("____________Ejercicio 1___________________")
# Ejercicio 1: Suma de Números Pares
# Escribe un programa que calcule la suma de los primeros N números pares.
# Pista: Utiliza una variable para llevar la cuenta de los números pares y otra para acumular la suma.
numero_inicial = 2
numero_par_suma = 0

while numero_inicial <= 10:
    numero_par_suma +=numero_inicial

    numero_inicial +=2

print("La suma de los numero pares son: "+str(numero_par_suma))



print("____________Ejercicio 2___________________")
# Ejercicio 2: Adivina el Número
# Crea un juego en el que el programa genera un número aleatorio y el usuario debe adivinarlo. El juego debe dar pistas como "más alto" o "más bajo" después de cada intento.

# Pista: Usa un bucle while para permitir que el usuario realice múltiples intentos hasta que adivine el número.
#Asignar numero leatorio
numero_aleatorio = 3
print("ADIVINA EL NUMERO")

#Bucle para los intentos de adivinar
while True:
    #El usuario asigna el número que será adivinado
    numero_adivinar = int(input("Ingrese el numero adivinar: "))
    #Si son iguales los numeros el usuario gana
    if numero_adivinar == numero_aleatorio:
        print("Felicidades el numero "+str(numero_adivinar)+" es correcto")
        break
    #si el numero adivinar es alto envia una pista al usuario 
    elif numero_adivinar < numero_aleatorio:
        print("""***PISTA***
              El numero adivinar es 'MÁS ALTO'
              Vuelva a intentarlo
              __________________________________\n""")
    #si el numero es bajo adivinar envia una pista al usuario
    else:
         print("""***PISTA***
              El numero adivinar es 'MÁS BAJO'
               Vuelva a intentarlo
               ___________________________________\n""")



print("____________Ejercicio 3___________________")
# Ejercicio 3: Factorial
# Escribe un programa que calcule el factorial de un número dado.
# Pista: Utiliza una variable para el resultado y otra para el contador, y actualiza ambas en cada iteración del bucle.
numero_asignado = int(input("Asigne el número para calcular su Factorial: "))
contador = 1
resultado = 1

while contador <= numero_asignado:
    resultado *=contador
    contador +=1 
print("El factoria de "+str(numero_asignado)+" es: "+str(resultado))


print("____________Ejercicio 4___________________")
# Ejercicio 4: Serie Fibonacci
# Genera los primeros N términos de la serie Fibonacci.
# Pista: Utiliza tres variables para representar los términos anteriores y actuales en la serie y actualízalas en cada iteración del bucle
numero_anterior = 0
numero_actual = 1
serie = [numero_anterior, numero_actual]

cantidad_numeros = int(input('Ingrese la cantidad de series de Fibonacci: '))

while  len(serie) < cantidad_numeros:
    res_siguiente =  numero_actual + numero_anterior
    serie.append(res_siguiente)
    numero_anterior = numero_actual
    numero_actual = res_siguiente

print('Serie Fibonacci de ',cantidad_numeros, 'terminos :',serie)

