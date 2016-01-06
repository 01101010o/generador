#!/usr/bin/env python
##...Creado por 01101010o...##

class GENERADOR():
	def __init__(self,x1,x2,s0,s1,s2):
		self.x1=x1
		self.x2=x2
		self.s0=s0
		self.s1=s1
		self.s2=s2
# Efecto s0 --> acompaña al termino cuadratico # XXX implementar modulo en gen_b
	def cs1(self):
		if self.s0==1:
			if self.s1==0:
				return 1
			else:
				return 0
		else:
			return self.s1
	def cs2(self):
		if self.s0==1:
			if self.s2==0:
				return 1
			else:
				return 0
		else:
			return self.s2

# Genera terminos de la ecuacion
	def gen_b(self):
		cs2=GENERADOR.cs2(self)
		if cs2==0:
			b=self.x1+self.x2
		else:
			b=abs(self.x1-self.x2)
		return b

	def gen_c(self):
		return self.x1*self.x2

# Genera los signos de las soluciones
	def ss1(self):
		cs1=GENERADOR.cs1(self)
		cs2=GENERADOR.cs2(self)
		if cs2==0:
			if cs1==0:
				return 1
			else:
				return 0
		else:
			if cs1==0:
				if self.x1<self.x2:
					return 0
				else:
					return 1
			else:
				if self.x1<self.x2:
					return 1
				else:
					return 0				
	def ss2(self):
		cs1=GENERADOR.cs1(self)
		cs2=GENERADOR.cs2(self)
		if cs2==0:
			if cs1==0:
				return 1
			else:
				return 0
		else:
			if cs1==0:
				if self.x1<self.x2:
					return 1
				else:
					return 0
			else:
				if self.x1<self.x2:
					return 0
				else:
					return 1
