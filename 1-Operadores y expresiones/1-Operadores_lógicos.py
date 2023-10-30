#Negación del operador NOT

print( not True)
print(not True == False)
#Conjucion: Conjunto. sinónimo de union, contiguo o cercano. Agrupa uniendo.
#Disyución: Disyunto. Sinónimo de separado, apartado o distante. Agrupado separado.
print(True and True)
print(True and False)
print(False and False)

#Nos devulve un TRUE ya que la sentencia cumple lo que compara
a =15
print(a > 13 and  a < 20)

#Operador lógico en una cadena con AND
c = "Hola mundo"
print(len(c) >= 5 and c[0] == "H" )

#Operador logico en una cadena con OR
print(True or True)
print(True or False)
print(False or False)

d = "SALIR"
print(d == "EXIT" or d =="FIN" or d == "SALIR")

letra = "HOLA"
print(letra[0] == "H" or letra[0] == "h")
