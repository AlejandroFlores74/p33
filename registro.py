class Proyecto:
    def __init__(self, numero, fecha, titulo, lenguaje, cant_lineas):
        self.numero = numero
        self.fecha = fecha
        self.titulo = titulo
        self.lenguaje = lenguaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        res = "Número: " + str(self.numero) + ", fecha: " + str(self.fecha) + ", titulo: " + str(self.titulo) + \
              ", lenguaje: " + str(self.lenguaje) + ", cant_lineas: " + str(self.cant_lineas)
        return res


