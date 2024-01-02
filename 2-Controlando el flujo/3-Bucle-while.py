#¿Que es la iteración? Es ralizar una determinada acción varias veces. Cada vez que se repite la acción se denomina iteración 

#La magia de las iteraciones, que para econtrar un elemento, el ordenador debe recorrer los registros y compararlos hasta encontrar el que se busca.

#Sentencia while (Mietras): Se basa en repetir un bloque a patir de evaluar una codición lógica, siempre que ésta sea True. Por ello es que debemos planificar un momento en que la condición cambie a False y el while finalice su ejecución.
c = 0
while c <= 5:
    c += 1
    print("C vale: ",c)

q = 0
while q <= 4:
    q+= 1
    if q <= 2:
        print("Q vale "+str(q)+", rompemos el bucle con un break")
        break
    print("Q vale: ",q)
else: 
    print("Se ha completado toda la iteracion y q vale: ",q)


valor = 0 
while valor <= 7:
    valor+= 1
    if valor == 3:
        print("Continua a pesaar de que 3 sea igual a valor")
        continue
    print("Valor vale ",valor)
else:
    print("Se ha completado toda la iteracion y valor vale" ,valor)

print("______________________________________")

print("Bienvenidos a Practica Operaciones")
while(True):
    print("""Seleccion la opcion que desea realizar
          1)Multiplicación
          2)Suma
          3)Resta
          4)División
          5)Salir""")
    opcion = input("Opcion: ")
    if opcion == "1":
        numeroX = float(input("Introduce el primer numero: "))
        numeroY = float(input("Introduce el segundo numero: "))
        print("La multiplicación de "+str(numeroX)+" X "+str(numeroY)+" es: "+str(numeroX*numeroY))
    elif opcion == "2":
         numeroX = float(input("Introduce el primer numero: "))
         numeroY = float(input("Introduce el segundo numero: "))
         print("La suma de "+str(numeroX)+" + "+str(numeroY)+" es: "+str(numeroX+numeroY))
    elif opcion == "3":
         numeroX = float(input("Introduce el primer numero: "))
         numeroY = float(input("Introduce el segundo numero: "))
         print("La resta de "+str(numeroX)+" - "+str(numeroY)+" es: "+str(numeroX-numeroY))
    elif opcion == "4":
         numeroX = float(input("Introduce el primer numero: "))
         numeroY = float(input("Introduce el segundo numero: "))
         print("La división de "+str(numeroX)+" / "+str(numeroY)+" es: "+str(numeroX/numeroY))
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no valido, vuelva a intentarlo")