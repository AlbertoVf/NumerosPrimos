import math


def esPrimo(n) -> bool:
    '''
    Comprueba si un numero es primo
    :param n: Numero a comprobar
    :return: True o False dependiendo de si es primo
    '''
    nPrimos = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            nPrimos += 1
            if nPrimos > 1:
                return False
    return True


def listaPrimos(i, f) -> list:
    '''
    Crea una lista de numeros primos
    :param i: Inicio de la lista, incluido en la comprobacion
    :param f: Fin de lista, excluido de la comprobacion
    :return: lista con los numeros primos
    '''
    lista = []
    for n in range(i, f):
        if esPrimo(n):
            lista.append(n)
    return lista
