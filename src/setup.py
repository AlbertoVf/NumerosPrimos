from src.calculos import continuarCalculos

datos = {
    'inicio': 12 * 100 * 1000 * 1000,
    'final': 13 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}
continuarCalculos(datos['final'], datos['incremento'])
