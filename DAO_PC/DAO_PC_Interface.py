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
            if(int(c.find("id").text) == id):
                computador.setTipoComputador(c.find("tipo").text)
                computador.setDescripcion(c.find("descripcion").text)
                computador.setImagen(c.find("imagen").text)
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


    def GetAllPartesXML(self, idComputador):
        partes = Parte()
        conexion = XmlConexion.get_conexion(self)
        arregloPartes = []
        
        for c in conexion:
            if(int(c.find("id").text) == idComputador):
                if(c.find("partes").tag == "partes"):
                    for parte in c.find("partes"):
                        arregloPartes.append(parte.find("parte").text)
        
        partes.setNombreParte(arregloPartes)
        return arregloPartes