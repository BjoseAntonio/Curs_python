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
  print(i," * ",numero_mult," = ", total)
