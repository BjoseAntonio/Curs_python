while(True):
  resultado =  input('1 o 2: ')
  if resultado == '1':
    # 1.- Suma de Números Pares:
    # Problema: Escribe un programa que calcule la suma de los primeros n números pares, donde n es ingresado por el usuario.
    # Pista: Utiliza el operador % para verificar si un número es par.

    numero = int(input("Escribe un numero: "))
    suma = 0
    suma_impar = 0

    for i in range(numero+1):
      if i % 2 == 0:
        suma += i
      # else:
      #   suma_impar += i


    print("Suma numero par: ",suma)
    # print("Suma numero impar: ",suma_impar)

    # 2.- Tabla de Multiplicar:
    # Problema: Escribe un programa que solicite al usuario ingresar un número e imprima la tabla de multiplicar de ese número del 1 al 10.
    # Pista: Utiliza un bucle for para iterar del 1 al 10.
    numero_mult = int(input("Ingrese un nunero a multiplcar: "))
    total = 0

    for i in range(10+1):
      total = numero_mult * i
      print(f"{i} * {numero_mult} = {total}")

    # 3- Factorial de un Número:
    # Problema: Escribe un programa que calcule el factorial de un número ingresado por el usuario.
    # Pista: Utiliza un bucle for y acumula el resultado en cada iteración.
      
    n_factorial = int(input('Escribe un número para obtener su factorial: '))
    resultado_iteracion = 1
    valor_ini_mul = 0
    for i in range(1, n_factorial+1):
      valor_ini_mul = resultado_iteracion
      resultado_iteracion *= i

      print(f'Indice: {i} valor: {valor_ini_mul}  resultado: {resultado_iteracion}')
      print('___________________') 

    # 4- Contador de Vocales:
    # Problema: Escribe un programa que cuente el número de vocales en una palabra ingresada por el usuario.
    # Pista: Utiliza un bucle for para recorrer cada letra de la palabra.
    palabra = input('Escribe una palabra: ')
    contador_volcales= 0
    contador_caracteres = 0
    for caracter in palabra:
      if caracter.lower() in 'aeiou':
        contador_volcales +=1

      contador_caracteres +=1
      if caracter == " ":
        contador_caracteres -= 1
    print(f"la cantidad de vocales en la palabra '{palabra}' son de {contador_volcales} con una cantidad de caracteres de {contador_caracteres}")

   # 5-  Secuencia Fibonacci:
   # Problema: Escribe un programa que genere los primeros n términos de la secuencia Fibonacci, donde n es ingresado por el usuario.
   # Pista: Utiliza un bucle for y dos variables para almacenar los términos previos.
    n_series = int(input("Escriba el número determinado para la serie Fibonacci: "))
    x, y = 0, 1
    resultado_secuencial = [x, y]
    
    for i in range(n_series):
      if len(resultado_secuencial) < n_series:
         x, y = y, x + y
         resultado_secuencial.append(y)

    print("Numero determinado de la serie es de  ",n_series," con un resultado como",resultado_secuencial)

  else:
    break

