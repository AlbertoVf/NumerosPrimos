def esPrimo(n):
    '''
    Comprueba si un numero es primo
    :param n: Numero a comprobar
    :return:
    '''
    nPrimos = 0
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            nPrimos += 1
            if nPrimos > 1:
                return False
    return True


def listaPrimos(i, f):
    '''
    Crea una lista de numeros primos
    :param i: Inicio de la lista, incluido en la comprobacion
    :param f: Fin de lista, excluido de la comprobacion
    :return:
    '''
    lista = []
    for n in range(i, f):
        if esPrimo(n):
            lista.append(n)
    return lista
