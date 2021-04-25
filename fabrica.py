#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from partes import *

class FabricaAbstracta(ABC):

    @abstractmethod
    def crearComputador(self, id, conexion):
        pass

class FabricaComputadores(FabricaAbstracta):

    def crearComputador(self, id, conexion):
        return DevolverPc.getComputadorPartes(self, id, conexion)