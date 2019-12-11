import time

from src.primos import listaPrimos

ficheroCSV = '../Primos/Informacion.csv'
ficheroJSON = '../Primos/Informacion.json'


def escribirPrimos(archivo, datos):
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
    escribirPrimos(archivo, listaPrimos(i, f))


def obtencionDatos(tituloRango):
    '''
    Agrega a un fichero csv informacion sobre el rango de numeros primos analizado
    :param tituloRango: rango de numeros primos con el formato <inicio a fin>
    :return: Array con los datos
    '''

    inicioRango, finRango = tituloRango.split(' a ')
    a = time.time()
    lista = listaPrimos(int(inicioRango), int(finRango))
    b = time.time()
    duracion = str(float(b - a))
    return {"Rango": tituloRango, "Numero de primos": len(lista), "Duracion": duracion}


def ImpresionAvance(fichero):
    '''
    Imprime en consola informacion sobre el avance de la creacion de ficheros
    :param fichero: Nombre del fichero
    :return: Impresion por pantalla con informacion sobre la hora y el nombre del fichero que se creara
    '''
    print(time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)


def resumenDatos():
    '''
    Imprime en pantalla informacion sobre el fichero
    :return:
    '''
    file = open(ficheroCSV)
    file.readline()
    nInicio = file.readline().split(' a ')[0]
    nFin = ""
    duracionS = float(0)
    nPrimos = 0
    nLineas = 1
    for e in file:
        nLineas += 1
        cont = e.rstrip().split(';')
        if cont[1].isdigit():
            nPrimos += int(cont[1])
            duracionS += float(cont[2].replace(',', '.'))
            nFin = cont[0].split(' a ')[1]

    duracionE = str(int(duracionS / 3600)) + " h " + str(int((duracionS / 60) % 60)) + " min " + str(duracionS % 60) + " seg."
    print(
        "Inicio: " + str(nInicio)
        + "\nFin: " + str(nFin)
        + "\nNº lineas: " + str(nLineas, )
        + "\nNumeros Primos: " + str(nPrimos)
        + "\nDuracion: " + str(duracionS) + " seg.\t(" + str(duracionE) + ")"
    )


def exportarCSV(datos):
    '''
    Agrega una nueva linea a un fichero csv con informacion sobre el rango de primos calculado
    :param datos: Array con los datos que se escribiran en el csv
    :return:
    '''
    file = open(ficheroCSV, "a+")
    file.write("\n" + datos["Rango"] + ";" + str(datos["Numero de primos"]) + ";" + str(datos["Duracion"].replace('.', ',')))
    file.close()
