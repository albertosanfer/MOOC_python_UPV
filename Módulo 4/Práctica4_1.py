# Crea una variable de nombre par de tipo cadena que contenga todos los numeros
# pares del 1 al 86 concatenados uno detrás de otro (tipo "24681012....") y una
# variable de nombre impar también de tipo cadena que contenga los impares.
# Pista: puedes usar el comando range(1,87)

par = ""
impar = ""

for numero in list(range(1,87)):
    if numero%2 == 0:
        par = par + str(numero)
    else:
        impar = impar + str(numero)
print(par)
print(impar)
