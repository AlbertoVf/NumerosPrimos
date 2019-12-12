from src.calculos import continuarCalculos

datos = {
    'inicio': 1023 * 1000 * 1000,
    'final': 1100 * 1000 * 1000,
    'incremento': 1000 * 1000
}
continuarCalculos(datos['final'], datos['incremento'])
