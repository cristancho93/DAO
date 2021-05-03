#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC

from DAO_PC.DAO_PC_Interface import ComputadorDAO

class DevolverPc(ABC):
    def getComputadorPartes(self, id, conexion):
        if(conexion == 0):
            return ComputadorDAO.GetComputadorJSON(self ,id)
        else:
            return ComputadorDAO.GetComputadorXML(self, id)


class DevolverPartes(ABC):
    def getPartes(self,idComputador, conexion):
        if(conexion == 0):
             return ComputadorDAO.GetAllPartesJSON(self, idComputador)
        else: 
            return ComputadorDAO.GetAllPartesXML(self, idComputador)

class DevolverParte(ABC):
    def getParte(self, idComputador, idPartes, conexion):
        if conexion == 0:
            return ComputadorDAO.GetParteById(self, idComputador, idPartes)
        else:
            return ComputadorDAO.GetParteByIdXML(self, idComputador, idPartes)
