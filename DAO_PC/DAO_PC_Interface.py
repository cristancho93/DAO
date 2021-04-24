class ComputadorDAO:
    def GetComputador(id):
        computador = Computador()
        JsonConexion = JsonConexion();
        computadores = JsonConexion.get_conexion()

        for c in computadores:
            if(c.id == id):
                computador.setMemoria(c.memoria)
                computador.setBoard(c.board)
                computador.setProcesador(c.procesador)
                computador.setImagen(c.imagen)
                computador.setDescripcion(c.descripcion)
        return computador



