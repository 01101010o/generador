#!/usr/bin/env python
##...Creado por 01101010o...##
#----------------------Módulos
import random

class GENERADOR():
	def __init__(self,x1,x2,s1,s2):
		self.x1=x1
		self.x2=x2
		self.s1=s1
		self.s2=s2

	def gen_b(self):
		if self.s2==0:
			b=self.x1+self.x2
		else:
			b=abs(self.x1-self.x2)
		return b

	def gen_c(self):
		return self.x1*self.x2

	def ss1(self):
		if self.s2==0:
			if self.s1==0:
				return 1
			else:
				return 0
		else:
			if self.s1==0:
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
		if self.s2==0:
			if self.s1==0:
				return 1
			else:
				return 0
		else:
			if self.s1==0:
				if self.x1<self.x2:
					return 1
				else:
					return 0
			else:
				if self.x1<self.x2:
					return 0
				else:
					return 1
