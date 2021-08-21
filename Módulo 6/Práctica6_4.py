# Escribe una función cambiamayus que dadas una cadena nos devuelva la misma
# cadena cambiando las mayusculas por minúsculas y viceversa

def cambiamayus(cadena):
    resultado = ""
    for letra in cadena:
        if letra.islower():
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado

texto = input ('Introduce un texto: ')
print(cambiamayus(texto))
