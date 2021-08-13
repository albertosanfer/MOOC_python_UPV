# En el siguiente fragmento de código tenemos un input en el que le solicitamos
# al usuario cuantos litros de agua se ha bebido hoy y se los vamos a restar a
# la variable \"aguaEnDeposito\" de modo que tendremos un control de cuando
# comprar agua.

# Realiza una conversión del tipo de datos del input para que sea de tipo int y
# asígnalo a la variable consumo de modo que podamos hacer la resta.

# modifica el código a continuación para que el resultado final sea el
# solicitado en el enunciado,

aguaEnDeposito = 50
consumo = input ('¿Cuantos litros de agua has consumido hoy?')
resultado = aguaEnDeposito - int(consumo)
print(resultado)
