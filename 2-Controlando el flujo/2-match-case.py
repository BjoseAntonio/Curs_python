#Match-case es lo mismo que switch-case pero añadido en python 3.10 como un nueva sentencia condicional 
#Ejemplo 
opcion = input("Selecciona una ocpión A, B o C: ")

match opcion:
    case "A":
        print("Seleccionaste la opcion A")
    case "B":
        print("Seleccionaste la opcion B")
    case "C": 
        print("Seleccionaste la opcion C")
    case _:
        print("No coicide la opción")
