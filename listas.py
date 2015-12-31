#!/usr/bin/env python
# -*- coding: utf-8 -*-
##...Creado por 01101010o...##
#----------------------Módulos
def recorrersum(lista,salida):
	for z in lista:
		salida=salida+z
	return salida
def eliminar(lista,posicion,condicion):
	if lista[posicion] == condicion:
		del lista[posicion]
	return lista
def eliminarUNO(lista,x):
	for i in range(len(lista)-1):
		if lista[i] == x:
			if lista[i-1] == '1':
				del lista[i-1] # XXX Crear una lista con las posiciones, NO ELIMINAR, dar vuelta la lista, y luego eliminar todas las posiciones guardadas
	return lista
