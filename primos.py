import time


def esPrimo(n):
    '''
    Comprueba si un numero es primo
    :param n: Numero a comprobar
    :return:
    '''
    nPrimos = 0
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            nPrimos += 1
            if nPrimos > 1:
                return False
    return True


def listaPrimos(i, f):
    '''
    Crea una lista de numeros primos
    :param i: Inicio de la lista, incluido en la comprobacion
    :param f: Fin de lista, excluido de la comprobacion
    :return:
    '''
    lista = []
    for n in range(i, f):
        if esPrimo(n):
            lista.append(n)
    return lista


def escribirArchivo(archivo, datos):
    '''
    Agrega los numeros primos localizados al fichero, separandolos por espacios
    :param archivo: Nombre del archivo
    :param datos: Lista de numeros primos
    :return:
    '''
    file = open(archivo, "w")
    for e in datos:
        file.write(str(e) + " ")
    file.close()


def creacionFichero(i, f):
    '''
    Crea el fichero de numeros primos con el nombre correspondiente al rango de comprobacion
    :param i: Inicio del rango
    :param f:  Fin del rango
    :return: Volcado de numeros primos en el fichero
    '''
    archivo = "Numeros Primos desde " + str(i) + " a " + str(f) + ".txt"
    escribirArchivo(archivo, listaPrimos(i, f))


def calculadora(inicio, final, incremento):
    '''
    Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
    :param inicio: Numero por el que comienza a buscar los numeros primos
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return: Fichero .txt con los numeros primos
    '''
    while (inicio < final):
        print("--\n" + time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero")
        creacionFichero(inicio, inicio + incremento)
        hora = time.strftime("%H.%M.%S", time.localtime())
        print(hora + " - Fichero creado " + str(inicio // incremento + 1) + "/" + str(final // incremento))
        inicio += incremento


def calculadora(inicio, incremento):
    '''
    Crea ficheros infinitos en los que comprueba los numeros primos
    :param inicio: Inicio del rango de comprobacion
    :param incremento: Limite del rango que se guardara en un mismo archivo
    :return:
    '''
    inf = 1
    while (inf == 1):
        print("--\n" + time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + str(
            inicio) + " a " + str(inicio + incremento))
        creacionFichero(inicio, inicio + incremento)
        inicio += incremento
