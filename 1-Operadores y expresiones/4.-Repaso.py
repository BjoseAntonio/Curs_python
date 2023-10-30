n = 0 #Asignacio de 0 en n
while n < 10: #Expresion relacional donde n es menor que 10, devolviendo "True"
    if (n % 2) == 0: #Expresión aritmética (n Modulo de 2) y despues una expresión relacional 
        print(n,"Es un número par ")
    else:
        print(n,"Es un número impar ")
    n += 1 #Expresión aritmética n = n + 1 Equivalente a operación en asignación n+= 1
    
