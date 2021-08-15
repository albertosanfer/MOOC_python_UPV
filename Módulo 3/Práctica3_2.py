# Usando el comando input guardaremos en la variable \"primero\" un número
# entero que le solicitaremos al usuario.
# Usando el comando input guardaremos también en la variable \"segundo\" un
# número entero que le solicitaremos al usuario.
# Finalmente deberemos guardar en la variable \"mayor\" el número mayor de los
# 2 solicitados.
# Nota, acordaros de realizar la conversión de tipos en el input.

primero = int(input('Introduce un número:'))
segundo = int(input('Introduce un número:'))
if primero > segundo:
    mayor = primero
else:
    mayor = segundo
print(mayor)
