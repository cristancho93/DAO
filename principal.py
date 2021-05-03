#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabrica import *
from Util.JSONconexion import JsonConexion

if __name__ == '__main__':
    # Devolvemos el computador
    print("seleccione una fabrica: \n\t 0 - AMD \n\t 1 - Intel \n\t 2 - Alien ")
    pc = int(input())
    if pc == 0 or pc == 1 or pc == 2:
        print("seleccione una conexion: \n\t 0 - JSON \n\t 1 - XML ")
        conexion = int(input())
        fabrica = FabricaComputadores()
        computador = fabrica.crearComputador(pc, conexion)

        print(computador.getTipoComputador())
        print(computador.getDescripcion())
        print(computador.getImagen())

        #Retornamos las partes del computador
        print("Ver partes del computador: \n\t 0 - Si \n\t 1 - No")
        decision = int(input())
        if decision == 0:
            partes = fabrica.crearPartes(pc, conexion)
            listaPartes = partes.getNombreParte()

            for p in listaPartes:
                print(p)
        else:
            exit()

        # Retornamos la descripcion de una parte del computador
        print("Ver detalles de una parte: \n\t 0 - Si\n\t 1 - No")
        decision2 = int(input())
        if decision2 == 0:
            print("¿Que parte desea consultar:?")
            for p in listaPartes:
                print(p)

            idParte = int(input())
            parte = fabrica.crearParte(pc, idParte, conexion)
            print(parte.getNombreParte())
            print(parte.getDescripcionParte())
        else:
            exit()
    else:
        print("ERROR - Selección errada!")
        exit()