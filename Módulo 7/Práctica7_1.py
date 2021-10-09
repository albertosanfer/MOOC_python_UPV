#La función primerafrase(numerodeparrafo) deberá abrir el archivo y devolver el
#contenido de la primera frase del párrafo indicado (siendo 0 el primer
#párrafo). La primera frase estará definida por los caracteres que se
#encuentran en el párrafo hasta llegar al primer símbolo de puntuación
#(cualquiera del grupo ,.:;),

 def primerafrase(parrafo):
     fichero = open('qijote.txt')
     texto = fichero.read()
     parrafos = texto.split('\n')
     while '' in parrafos:
        parrafos.remove('')
    parrafoseleccionado=parrafos[parrafo]
    delimitadores =[]
    delimitadores.append(parrafoseleccionado.find(','))
    delimitadores.append(parrafoseleccionado.find('.'))
    delimitadores.append(parrafoseleccionado.find(':'))
    delimitadores.append(parrafoseleccionado.find(';'))
    while -1 in delimitadores:
        delimitadores.remove(-1)
    finfrase = min(delimitadores)
    frase = parrafoseleccionado[:finfrase]
    print(frase)
    fichero.close()
    return(frase)
