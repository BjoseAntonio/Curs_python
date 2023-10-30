#Utilizando una condición if-elif-else debes realizar un programa que compare la longitud de dos variables (cadena_1 y cadena_2) y en función del resultado almacene un valor en otra variable llamada resultado:

#Si cadena_1 es más larga que cadena_2 la variable resultado deberá tener el valor entero 1.

#Si cadena_1 es más corta que cadena_2 la variable resultado deberá tener el valor entero 2.

#Si cadena_1 tiene la misma longitud que cadena_2 la variable resultado deberá tener el valor entero 0.

cadena_1 = "Hola"
cadena_2 = "Hola"
resultado = 0

if  len(cadena_1) > len(cadena_2):
    resultado += 1
    print(resultado)
elif len(cadena_1) < len(cadena_2):
    resultado += 2
    print(resultado)
else:
    print(resultado)