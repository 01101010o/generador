#!/usr/bin/env python
##...Creado por 01101010o...##
#----------------------Módulos
import random
from byte_signo import BYTE_SIGNO
from gen_b_c import GENERADOR

class ECU2(BYTE_SIGNO,GENERADOR):
	def __init__(self, r, nombre):
		self.r=r
		self.nombre=nombre
	def Enunciado(self):
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\section{Encontrar las soluciones de:}');
		archivo.close()
	def Ejercicios(self):
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\begin{enumerate}');
		for i in range(1, self.r+1):
			x1=random.randrange(10)
			x2=random.randrange(10)
			s1=random.randrange(2)
			s2=random.randrange(2)
			signo1=BYTE_SIGNO(s1)
			signo2=BYTE_SIGNO(s2)
			gen=GENERADOR(x1,x2,s1,s2)
			b=gen.gen_b()
			c=gen.gen_c()
			ss1=BYTE_SIGNO(gen.ss1())
			ss2=BYTE_SIGNO(gen.ss2())
			if b==0:
				if c==0:
					archivo.write('\\item$x^2=0$\\\\');
				else:
					archivo.write('\\item$x^2'+signo2.Signo()+str(c)+'=0$\\\\');
			elif b==1:
				if c==0:
					archivo.write('\\item$x^2'+signo1.Signo()+'x=0$\\\\');
				else:
					archivo.write('\\item$x^2'+signo1.Signo()+'x'+signo2.Signo()+str(c)+'=0$\\\\');
			else:
				if c==0:
					archivo.write('\\item$x^2'+signo1.Signo()+str(b)+'x=0$\\\\');
				else:
					archivo.write('\\item$x^2'+signo1.Signo()+str(b)+'x'+signo2.Signo()+str(c)+'=0$\\\\');
			print(ss1.Signo()+str(x1),ss2.Signo()+str(x2))
		archivo.write('\\end{enumerate}')
		archivo.close()
