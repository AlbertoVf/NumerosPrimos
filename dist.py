import datetime
import math
import time

ruta = '../Primos/'
ficheroCSV = ruta + 'Informacion.csv'
datos = {
    'inicio': 62 * 100 * 1000 * 1000,
    'final': 63 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}

def escribirPrimos(archivo, datos) -> None:
    file = open(ruta + archivo, "w")
    for e in datos:
        file.write(str(e) + " ")
    file.close()


def creacionFichero(tituloRango) -> dict:
    inicioRango, finRango = tituloRango.split('-')
    archivo = "primos-" + str(inicioRango) + "-" + str(finRango) + ".txt"
    a = time.time()
    lista = listaPrimos(int(inicioRango), int(finRango))
    b = time.time()
    escribirPrimos(archivo, lista)
    duracion = str(float(b - a))
    return {"Rango": tituloRango, "Numero de primos": len(lista), "Duracion": duracion}


def ImpresionAvance(fichero) -> None:
    print(time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)


def resumenDatos() -> None:
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

    duracionE = datetime.timedelta(duracionS)
    print('Inicio: {}\nFin: {}\nNº lineas: {}\nNumeros primos: {}\nDuracion: {} seg.\t ({})'.format(nInicio, nFin,
                                                                                                    nLineas, nPrimos,
                                                                                                    duracionS,
                                                                                                    duracionE))


def exportarCSV(datos) -> None:
    file = open(ficheroCSV, "a+")
    file.write(
        "\n" + datos["Rango"] + ";" + str(datos["Numero de primos"]) + ";" + str(datos["Duracion"].replace('.', ',')))
    file.close()


def escribirPrimos(archivo, datos):
    file = open(ruta + archivo, "w")
    for e in datos:
        file.write(str(e) + " ")
    file.close()


def esPrimo(n) -> bool:
    nPrimos = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            nPrimos += 1
            if nPrimos > 1:
                return False
    return True


def listaPrimos(i, f) -> list:
    lista = []
    for n in range(i, f):
        if esPrimo(n):
            lista.append(n)
    return lista


def calculadora(inicio, final, incremento) -> None:
    while (inicio < final):
        fichero = str(inicio) + "-" + str(inicio + incremento)
        ImpresionAvance(fichero)
        exportarCSV(creacionFichero(fichero))
        inicio += incremento


def calculadoraInfinita(inicio, incremento) -> None:
    inf = 1
    while (inf == 1):
        fichero = str(inicio) + "-" + str(inicio + incremento)
        ImpresionAvance(fichero)
        exportarCSV(creacionFichero(fichero))
        inicio += incremento


def continuarCalculos(final, incremento) -> None:
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


continuarCalculos(datos['final'], datos['incremento'])
