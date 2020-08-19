import datetime
import time
import math
ruta = '../Primos/'
ficheroCSV = ruta + 'Informacion.csv'
datos = {
    'inicio': 62 * 100 * 1000 * 1000,
    'final': 63 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}


def escribirPrimos(archivo, datos):
    file = open(ruta + archivo, "w")
    for e in datos:
        file.write(str(e) + " ")
    file.close()


def esPrimo(n):
    nPrimos = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            nPrimos += 1
            if nPrimos > 1:
                return False
    return True


def listaPrimos(i, f):
    lista = []
    for n in range(i, f):
        if esPrimo(n):
            lista.append(n)
    return lista

def creacionFichero(tituloRango):
    inicioRango, finRango = tituloRango.split('-')
    archivo = "primos-" + str(inicioRango) + "-" + str(finRango) + ".txt"
    a = time.time()
    lista = listaPrimos(int(inicioRango), int(finRango))
    b = time.time()
    escribirPrimos(archivo, lista)
    duracion = str(float(b - a))
    return {"Rango": tituloRango, "Numero de primos": len(lista), "Duracion": duracion}


def ImpresionAvance(fichero):
    print(time.strftime("%H.%M.%S", time.localtime()) + " - Inicio de creacion de fichero de " + fichero)


def exportarCSV(datos):
    file = open(ficheroCSV, "a+")
    file.write("\n" + datos["Rango"] + ";" + str(datos["Numero de primos"]) + ";" + str(datos["Duracion"].replace('.', ',')))
    file.close()


def conversorSegundos(segundos):
    return str(datetime.timedelta(seconds=segundos))


def continuarCalculos(final, incremento):
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
