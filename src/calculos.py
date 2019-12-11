from src.informacion import creacionFichero, obtencionDatos, exportarCSV, ImpresionAvance


def calculadora(inicio, final, incremento):
    '''
    Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
    :param inicio: Numero por el que comienza a buscar los numeros primos
    :param final:  Ultimo numero que comprueba si es primo
    :param incremento: Rango de numeros que se introducira en el fichero
    :return: Fichero .txt con los numeros primos
    '''
    while (inicio < final):
        fichero = str(inicio) + " a " + str(inicio + incremento)
        ImpresionAvance(fichero)
        creacionFichero(inicio, inicio + incremento)
        exportarCSV(obtencionDatos(fichero))
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
        fichero = str(inicio) + " a " + str(inicio + incremento)
        ImpresionAvance(fichero)
        creacionFichero(inicio, inicio + incremento)
        exportarCSV(obtencionDatos(fichero))
        inicio += incremento
