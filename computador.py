class computador:
    def __init__(self):
        self.procesador = ""
        self.memoria = ""
        self.descripcion = ""
        self.board = ""
        self.imagen = ""

    def setMemoria(self, memoria):
        self.memoria = memoria

    def setBoard(self, board):
        self.board = board

    def setProcesador(self, procesador):
        self.procesador = procesador

    def setImagen(self, imagen):
        self.imagen = imagen

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion