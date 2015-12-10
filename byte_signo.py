#! /usr/bin/env python
#Relaciona el numero "0" con un '+'
#y el numero "1" con un '-'

class BYTE_SIGNO():
	def __init__(self,s):
		self.s=s
	def Signo(self):
		if self.s==0:
			return '+'
		else:
			return '-'
