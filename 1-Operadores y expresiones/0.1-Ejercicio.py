# En una lista llamada expresiones encontramos diferentes operaciones relacionales, ¿podrías determinar mentalmente el resultado de cada expresión y almacenarlo en una nueva lista llamada resultados? Esta lista debe contener únicamente valores lógicos True y False. Por ejemplo, supongamos esta lista:

# expresiones = [1 == 1, 1 < 0]
# La respuesta que se espera que escribas es:

# resultados = [True, False]
# Correspondiendo True al resultado de 1==1 y False al de 1<0,  es decir, los resultados deben concordar con la posición de las expresiones, siendo resultados[0] la respuesta a la expresión expresiones[0].

expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]
resultados = expresiones

print(resultados)