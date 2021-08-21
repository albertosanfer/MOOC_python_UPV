# Escribe una función enelmedio que dadas dos cadenas nos devuelva una sola
# cadena de modo que la segunda quede en el medio de la primera

def enelmedio(cadena1, cadena2):
    return cadena1[:divmod(len(cadena1),2)[0]] + cadena2 + \
    cadena1[divmod(len(cadena1),2)[0]:]

texto1 = input ('Introduce una cadena: ')
texto2 = input ('Introduce otra cadena: ')
print(enelmedio(texto1,texto2))
