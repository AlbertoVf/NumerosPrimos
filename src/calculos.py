import time

from src.informacion import creacionFichero, Tiempo


def calculadora(inicio, final, incremento):
    '''
    Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
    :param inicio: Numero por el que comienza a buscar los numeros primos
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return: Fichero .txt con los numeros primos
    '''
    while (inicio < final):
        a = time.time()
        fichero = str(inicio) + " a " + str(inicio + incremento)
        print("--\n" + time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)
        creacionFichero(inicio, inicio + incremento)
        b = time.time()
        Tiempo(fichero, a, b)
        inicio += incremento


def calculadoraInfinita(inicio, incremento):
    '''
    Crea ficheros infinitos en los que comprueba los numeros primos
    :param inicio: Inicio del rango de comprobacion
    :param incremento: Limite del rango que se guardara en un mismo archivo
    :return:
    '''
    inf = 1
    while (inf == 1):
        a = time.time()
        fichero = str(inicio) + " a " + str(inicio + incremento)
        print("--\n" + time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)
        creacionFichero(inicio, inicio + incremento)
        b = time.time()
        Tiempo(fichero, a, b)
        inicio += incremento
