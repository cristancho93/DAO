class Computador:
    def __init__(self):
        self.tipoComputador = "",
        self.descripcion = "",
        self.imagen = ""

    def setTipoComputador(self, tipoComputador):
        self.tipoComputador = tipoComputador

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setImagen(self, imagen):
        self.imagen = imagen


# Creamos lo get para retornar la información
    def getTipoComputador(self):
        return self.tipoComputador

    def getDescripcion(self):
        return self.descripcion

    def getImagen(self):
        return self.imagen