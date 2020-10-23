from src.informacion import creacionFichero, exportarCSV, ImpresionAvance, ficheroCSV


def calculadora(inicio, final, incremento) -> None:
    '''
    Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
    :param inicio: Numero por el que comienza a buscar los numeros primos
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return: Fichero .txt con los numeros primos
    '''
    while (inicio < final):
        fichero = str(inicio) + "-" + str(inicio + incremento)
        ImpresionAvance(fichero)
        exportarCSV(creacionFichero(fichero))
        inicio += incremento


def calculadoraInfinita(inicio, incremento) -> None:
    '''
    Crea ficheros infinitos en los que comprueba los numeros primos
    :param inicio: Inicio del rango de comprobacion
    :param incremento: Limite del rango que se guardara en un mismo archivo
    :return:
    '''
    inf = 1
    while (inf == 1):
        fichero = str(inicio) + "-" + str(inicio + incremento)
        ImpresionAvance(fichero)
        exportarCSV(creacionFichero(fichero))
        inicio += incremento


def continuarCalculos(final, incremento) -> None:
    '''
    Calcula los numeros primos a partir del ultimo rango que hay en el fichero
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return:
    '''
    file = open(ficheroCSV)
    for e in file:
        cont = e.rstrip().split(';')
        if cont[1].isdigit():
            inicio = cont[0].split('-')[1]
    inicio = int(inicio)
    while (inicio < final):
        fichero = str(inicio) + "-" + str(inicio + incremento)
        ImpresionAvance(fichero)
        exportarCSV(creacionFichero(fichero))
        inicio += incremento