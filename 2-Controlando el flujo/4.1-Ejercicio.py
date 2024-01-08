# En este ejercicio se te facilitará un numero aleatorio que no conoces en la variable numero.

# Utilizando lo que conoces sobre los bucles for y la función range() , debes realizar un sumatorio de todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples de 5 y 7, y almacenarlo en la variable sumatorio.

# Ejemplo, si numero fuera 7, el sumatorio sería igual a 1+2+3+4+6 = 16.

# Recuerda, únicamente debes sumar los números NO múltiples de 5 y 7 al sumatorio.


# multiplo = float(input('Ingrese un numero: '))
numero = 6
almacen_rango = 0


# if multiplo % numero == 0:
#     print("si es multiplo")
# else:
#     print("no es multiplo")

for i in range(numero+1):
    if i % 5 != 0 and i % 7 != 0:
        almacen_rango += i
        
print(almacen_rango)

    




#numero % multiplo == 0S
