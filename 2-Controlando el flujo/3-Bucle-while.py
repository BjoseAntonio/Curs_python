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
        print("Q vale 2, rompemos el bucle con un break")
        break
    print("Q vale: ",q)
else: 
    print("Se ha completado toda la iteracion y q vale: ",q)

