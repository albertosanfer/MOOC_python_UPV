# A continuación define la función cuentapalabras la cual tendrá 2 parámetros,
# el primer parámetro será un texto y el segundo una palabra.
# La función deberá devolver usando el comando return el número de veces que
# aparece la palabra dentro del texto en una variable de tipo entero.
# Devolverá 0 si no aparece ninguna vez.

def cuentapalabras(parametro1, parametro2):
    cuenta = 0
    for palabras in parametro1.split():
        if palabras == parametro2:
            cuenta = cuenta +1
    return cuenta

texto = 'Hola mundo Hola mundo'
palabra = 'mundo'
repite = cuentapalabras(texto, palabra)
print(f'La palabra aparece {repite} veces')
