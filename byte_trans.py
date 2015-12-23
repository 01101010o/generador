#! /usr/bin/env python
#Signo:
#	Relaciona el numero "0" con un '+' y el numero "1" con un '-'
#Literal:
#	Relaciona el numero "0" con '' y el numero "1" con 'x'

class BYTE_TRANS():	#antes BYTE_SIGNO() modificar otros modulos
	def __init__(self,s):
		self.s=s
	def Signo(self):
		if self.s==0:
			return '+'
		else:
			return '-'
	def Literal(self):
		if self.s==0:
			return ''
		else:
			return 'x'	#en el futuro agregar mas letras asignando una variable aleatoria
