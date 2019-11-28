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


def Tiempo(nInicio,nFin, tiempoInicio, tiempoFin):
    '''
    Crea una linea en un archivo csv con informacion sobre la creacion de numeros primos
    :param fichero: Rango de numeros primos
    :param tiempoInicio: tiempo en el que se inicia la comprobacion
    :param tiempoFin: tiempo en el que finaliza la escritura en el archivo
    :return:
    '''
    file = open('../Primos/Informacion.csv', "a+")
    separacion = ";"
    encabezado = str(nInicio)+" a "+str(nFin)
    p= len(listaPrimos(nInicio, nFin))
    duracion = str(float(tiempoFin - tiempoInicio))
    file.write("\n" + encabezado + separacion + str(p) + separacion + duracion + separacion)
    file.close()