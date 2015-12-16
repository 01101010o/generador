#!/usr/bin/env python
##...Creado por 01101010o...##
#Clase que se encarga de dar formato para crear documentos .tex
class FORMAT():
	def __init__(self,texto):
		self.texto=texto	#texto de entrada
	def e(self):	#entrega texto de salida para ejercicios
		return '\\item$'+self.texto+'$\\\\'
