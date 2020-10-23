import datetime
import time

from src.primos import listaPrimos

ruta = '../Primos/'
ficheroCSV = ruta + 'Informacion.csv'
ficheroJSON = ruta + 'Informacion.json'


def escribirPrimos(archivo, datos) -> None:
    '''
    Agrega los numeros primos localizados al fichero, separandolos por espacios
    :param archivo: Nombre del archivo
    :param datos: Lista de numeros primos
    :return:
    '''
    file = open(ruta + archivo, "w")
    for e in datos:
        file.write(str(e) + " ")
    file.close()


def creacionFichero(tituloRango) -> dict:
    '''
    Agrega a un fichero csv informacion sobre el rango de numeros primos analizado
    :param tituloRango: rango de numeros primos con el formato <inicio a fin>
    :return: Array con los datos
    '''

    inicioRango, finRango = tituloRango.split('-')
    archivo = f"primos-{inicioRango}-{finRango}.txt"
    a = time.time()
    lista = listaPrimos(int(inicioRango), int(finRango))
    b = time.time()
    escribirPrimos(archivo, lista)
    duracion = str(float(b - a))
    return {"Rango": tituloRango, "Numero de primos": len(lista), "Duracion": duracion}


def ImpresionAvance(fichero) -> None:
    '''
    Imprime en consola informacion sobre el avance de la creacion de ficheros
    :param fichero: Nombre del fichero
    :return: Impresion por pantalla con informacion sobre la hora y el nombre del fichero que se creara
    '''
    print(time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)


def resumenDatos() -> None:
    '''
    Imprime en pantalla informacion sobre el fichero
    :return:
    '''
    file = open(ficheroCSV)
    file.readline()
    nInicio = file.readline().split('-')[0]
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
            nFin = cont[0].split('-')[1]

    print(f'Inicio: {nInicio}\nFin: {nFin}\nNº lineas: {nLineas}\nNumeros primos: {nPrimos}\nDuracion: {duracionS} seg.\t ({datetime.timedelta(seconds = duracionS)})')


def exportarCSV(datos) -> None:
    '''
    Agrega una nueva linea a un fichero csv con informacion sobre el rango de primos calculado
    :param datos: Array con los datos que se escribiran en el csv
    :return:
    '''
    file = open(ficheroCSV, "a+")
    file.write(f"\n{datos['Rango']};{datos['Numerodeprimos']};{datos['Duracion']}")
    file.close()
