#Escribe una función cambiaprimera que dada una cadena nos devuelva la misma
#cadena pero reemplazando todas las veces que aparezca la primera letra por el
# símbolo $, excepto en esa primera letra.

def cambiaprimera(cadena):
    return cadena[0] + cadena[1:].replace(cadena[0],"$")

texto = input ('Intriduce una cadena de texto: ')
print(cambiaprimera(texto))
