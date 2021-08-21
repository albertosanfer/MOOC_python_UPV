# Escribe una función concatenamal que, dadas dos cadenas nos devuelva una sola
# cadena combinando ambas unidas por un espacio, pero cambiando las dos
# primeras letras de cada palabra.

def concatenamal(palabra1, palabra2):
    return palabra2[0:2] + palabra1[2:] + " " + palabra1[0:2] + palabra2[2:]

texto1 = input ('Introduce una palabra: ')
texto2 = input ('Introduce otra palabra: ')
print(concatenamal(texto1,texto2))
