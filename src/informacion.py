import time

from src.primos import listaPrimos


def escribirFichero(archivo, datos):
    '''
    Agrega los numeros primos localizados al fichero, separandolos por espacios
    :param archivo: Nombre del archivo
    :param datos: Lista de numeros primos
    :return:
    '''
    file = open('../Primos/' + archivo, "w")
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
    escribirFichero(archivo, listaPrimos(i, f))


def obtencionDatos(tituloRango):
    '''
    Agrega a un fichero csv informacion sobre el rango de numeros primos analizado
    :param tituloRango: rango de numeros primos con el formato <inicio a fin>
    :return:
    '''
    file = open('../Primos/Informacion.csv', "a+")
    separacion = ";"
    inicioRango, finRango = tituloRango.split(' a ')
    print("Inicio de obtencion de datos. Rango de valores: " + tituloRango)

    a = time.time()
    lista = listaPrimos(int(inicioRango), int(finRango))
    p = len(lista)
    b = time.time()

    duracion = str(float(b - a))
    file.write("\n" + tituloRango + separacion + str(p) + separacion + duracion + separacion)
    file.close()


def ImpresionAvance(fichero):
    '''
    Imprime en consola informacion sobre el avance de la creacion de ficheros
    :param fichero: Nombre del fichero
    :return:
    '''
    print("--\n" + time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)
