#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from partes import *

class FabricaAbstracta(ABC):

    @abstractmethod
    def crearComputador(self, id, conexion):
        pass

    def crearPartes(self, idComputador):
        pass

    def crearParte(self, idComputador, idParte):
        pass

class FabricaComputadores(FabricaAbstracta):

    def crearComputador(self, id, conexion):
        return DevolverPc.getComputadorPartes(self, id, conexion)

    def crearPartes(self, idComputador, conexion):
        return DevolverPartes.getPartes(self, idComputador, conexion)

    def crearParte(self, idComputador, idParte, conexion):
        return DevolverParte.getParte(self, idComputador, idParte, conexion)