class Parte:
    def __init__(self):
        self.nombreParte = [],
        self.descripcionParte = ""

    # Seteamos los valores
    def setNombreParte(self, nombreParte):
        self.nombreParte = nombreParte

    def setDescripcionParte(self, descripcionParte):
        self.nombreParte = descripcionParte

    # Creamos lo get para retornar la información
    def getNombreParte(self):
        return self.nombreParte

    def getDescripcionParte(self):
        return self.descripcionParte