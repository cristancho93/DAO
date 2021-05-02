from Util.XMLConexion import XmlConexion
from clases.computador import Computador
from Util.JSONconexion import JsonConexion
from clases.parte import Parte

class ComputadorDAO:
    def GetComputadorJSON(self ,id):
        computador = Computador()
        computadores = JsonConexion.get_conexion(self)

        for c in computadores:
            if(c['id'] == id):
                computador.setTipoComputador(c['tipo'])
                computador.setDescripcion(c['descripcion'])
                computador.setImagen(c['imagen'])
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

    # Metodo encargado de traer todas las partes de un computador
    def GetAllPartesJSON(self, idComputador):
        partes = Parte()
        conexion = JsonConexion.get_conexion(self)
        arregloPartes = []
        i = 0
        for p in conexion:
            if (p['id'] == idComputador):
                for part in conexion[idComputador]["partes"]:
                    arregloPartes.append( str(i) + " - " + part['parte'])
                    i = i + 1

        partes.setNombreParte(arregloPartes)
        return partes

    def GetParteById(self, idComputador, idParte):
        partes = Parte()
        conexion = JsonConexion.get_conexion(self)
        for p in conexion:
            if (p['id'] == idComputador):
                 part = conexion[idComputador]["partes"][idParte]
                 partes.setNombreParte(part["parte"])
                 partes.setDescripcionParte(part["descripcion"])
        return partes