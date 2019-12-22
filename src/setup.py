from src.calculos import continuarCalculos
datos = {
    'inicio': 20 * 100 * 1000 * 1000,
    'final': 21 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}
continuarCalculos(datos['final'], datos['incremento'])
