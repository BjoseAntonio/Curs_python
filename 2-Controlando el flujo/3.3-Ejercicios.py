while(True):
    numMultiplo = int(input("Introducce un numero: "))
    if 5 % numMultiplo == 0:
        print("El numero "+str(numMultiplo)+" si es multiplo de 5")
        break
    else:
        print("El numero "+str(numMultiplo)+" no es multiplo de 5")



# def es_multiplo(numero, multiplo):
#     return numero % multiplo == 0

# if es_multiplo(9,3):
#     print("Si es multiplo")
# else:
#     print("No es multiplo")