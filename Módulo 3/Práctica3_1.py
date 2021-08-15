# A continuación tenemos un input en el que le pediremos un número al usuario y
# lo guardaremos en la variable entrada. Después, deberemos guardar en la
# variable mayorQueTres el valor True si ese número es mayor que tres y False
# en caso contrario.
# Nota, acordaros de realizar la conversión de tipos en el input

entrada = int(input('Introduce un número:'))

if entrada > 3:
    mayorQueTres = True
else:
    mayorQueTres = False
print(mayorQueTres)
