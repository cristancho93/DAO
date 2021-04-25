from Util.XMLConexion import XmlConexion
from computador import Computador
from Util.JSONconexion import JsonConexion

class ComputadorDAO:
    def GetComputadorJSON(self ,id):
        computador = Computador()
        computadores = JsonConexion.get_conexion(self)

        for c in computadores:
            if(c['id'] == id):
                computador.setMemoria(c['memoria'])
                computador.setBoard(c['board'])
                computador.setProcesador(c['procesador'])
                computador.setImagen(c['imagen'])
                computador.setDescripcion(c['descripcion'])
        return computador

    def GetComputadorXML(self ,id):
        computador = Computador()
        computadores = XmlConexion .get_conexion(self)
        for c in computadores:
            esId = False
            for c2 in c:
                if(c2.text.strip() == str(id) or esId == True):
                    if (c2.tag == 'memoria'): computador.setMemoria(c2.text.strip())
                    if (c2.tag == 'board'): computador.setBoard(c2.text.strip())
                    if (c2.tag == 'procesador'): computador.setProcesador(c2.text.strip())
                    if (c2.tag == 'imagen'): computador.setImagen(c2.text.strip())
                    if (c2.tag == 'descripcion'): computador.setDescripcion(c2.text.strip())
                    esId = True
        return computador



