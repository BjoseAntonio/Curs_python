# Pide al usuario que introduzca un número entero por teclado entre 1 y 9 (ambos incluidos) y guárdalo en la variable numero. Debes asegurarte de que esa variable numero contiene un numero entero del 1 al 9, utiliza un bucle para repetir la lectura hasta que se cumpla esa condición.
while(True):
    numero = int(input('Ingrese un numero del 1 al 9: '))
    if numero >= 1 and numero <= 9:
        print("El número seleccionado esta dentro del rango de 1 al 9")
        break
    else:
        print("Intente otra ves")


# Genera una lista llamada multiplos que contenga los múltiplos de numero en el rango de 1 a 100 (ambos incluidos) utilizando la conversión de un range a list con un paso: list(range(Min,Max,Paso)).
        
multiplos = []

numero_multiplo = int(input("Ingrese un numero: "))

for i,v in  list(range(numero_multiplo,101, numero_multiplo)):
  print(i)
#   multiplos[i] = i

# print(multiplos)
