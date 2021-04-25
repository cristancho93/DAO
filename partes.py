#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import computador
from DAO_PC.DAO_PC_Interface import ComputadorDAO

class DevolverPc(ABC):
    def getComputadorPartes(self, id, conexion):
        if(conexion == 0):
            return ComputadorDAO.GetComputadorJSON(self ,id)
        else:
            return ComputadorDAO.GetComputadorXML(self, id)