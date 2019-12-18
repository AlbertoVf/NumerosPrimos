from src.calculos import continuarCalculos

datos = {
    'inicio': 16 * 100 * 1000 * 1000,
    'final': 17 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}
continuarCalculos(datos['final'], datos['incremento'])
