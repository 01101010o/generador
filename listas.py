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
	posiciones = []
	for i in range(len(lista)):
		if lista[i] == x:
			if lista[i-1] == '1':
				posiciones.append(i-1)
	for f in range(len(posiciones)-1, -1, -1):
		del lista[posiciones[f]]
	return lista
def eliminar0(lista): # Debe ser usado antes que los otros
	posiciones = []
	for i in range(len(lista)-1):
		if lista[i] == '0':
			posiciones.append(i-1)
			posiciones.append(i)
			posiciones.append(i+1)
	for f in range(len(posiciones)-1, -1, -1):
		del lista[posiciones[f]]
	return lista
