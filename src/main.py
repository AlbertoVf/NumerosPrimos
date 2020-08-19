from src.calculos import continuarCalculos

datos = {
    'inicio': 55 * 100 * 1000 * 1000,
    'final': 59 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}

continuarCalculos(datos['final'], datos['incremento'])