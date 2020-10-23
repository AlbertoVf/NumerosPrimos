from src.informacion import creacionFichero, exportarCSV, ImpresionAvance, ficheroCSV

def calc(inicio, incremento):
    fichero = f'{inicio}-{inicio + incremento}'
    ImpresionAvance(fichero)
    cf = creacionFichero(fichero)
    exportarCSV(cf)

def calculadora(inicio, final, incremento) -> None:
    '''
    Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
    :param inicio: Numero por el que comienza a buscar los numeros primos
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return: Fichero .txt con los numeros primos
    '''
    while (inicio < final):
        calc(inicio, incremento)
        inicio += incremento


def calculadoraInfinita(inicio, incremento) -> None:
    '''
    Crea ficheros infinitos en los que comprueba los numeros primos
    :param inicio: Inicio del rango de comprobacion
    :param incremento: Limite del rango que se guardara en un mismo archivo
    :return:
    '''
    while (True):
        calc(inicio, incremento)
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
        calc(inicio, incremento)
        inicio += incremento