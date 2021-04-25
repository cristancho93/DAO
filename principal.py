#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabrica import *
from Util.JSONconexion import JsonConexion

if __name__ == '__main__':
    print("seleccione una fabrica: \n\t 0 - AMD \n\t 1 - Intel \n\t 2 - Alien ")
    pc = int(input())
    print("seleccione una conexion: \n\t 0 - JSON \n\t 1 - XML ")
    conexion = int(input())
    fabrica = FabricaComputadores()
    computador = fabrica.crearComputador(pc, conexion)

    print(computador.getMemoria())
    print(computador.getBoard())
    print(computador.getProcesador())
    print(computador.getImagen())
    print(computador.getDescripcion())