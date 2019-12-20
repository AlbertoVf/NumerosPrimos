from src.calculos import continuarCalculos
datos = {
    'inicio': 17 * 100 * 1000 * 1000,
    'final': 18 * 100 * 1000 * 1000,
    'incremento': 1000 * 1000
}
continuarCalculos(datos['final'], datos['incremento'])
