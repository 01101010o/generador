#!/usr/bin/env python
##...Creado por 01101010o...##
#Genera ecuaciones de segundo grado aleatorias en base a 2 soluciones enteras aleatorias

import random
from byte_trans import BYTE_TRANS  # Se encarga de la convercion Byte a texto
from gen_b_c import GENERADOR  # Se encarga de generar valores aleatorios para b,c, ademas de los signos para las soluciones.
from formatotex import FORMAT  # Se encarga de dar formato para latex
from listas import recorrersum, eliminar, eliminarUNO # , eliminar0

class ECU2(BYTE_TRANS,GENERADOR,FORMAT):
	def __init__(self, r, nombre): # Recibe como parámetros:
		self.r=r # La cantidad de ejercicios 'r'
		self.nombre=nombre # El nombre del archivo 'nombre'
	def Enunciado(self): # Modulo encargado de imprimir el enunciado para los ejercicios
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\section{Encontrar las soluciones de:}');
		archivo.close()
	def Ejercicios(self): # Modulo encargado de imprimir en el archivo .tex los ejercicios
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\begin{enumerate}');
		for i in range(1, self.r+1):
			x1=random.randrange(10) # Genera una solución entre 0-9
			x2=random.randrange(10)	# Genera la segunda solución entre 0-9
			s1=random.randrange(2)	# Genera un signo aleatorio
			s2=random.randrange(2)	
			signo1=BYTE_TRANS(s1)	
			signo2=BYTE_TRANS(s2)
			gen=GENERADOR(x1,x2,s1,s2)
			b=gen.gen_b() # Genera el valor que acompaña a la incógnita
			c=gen.gen_c() # Genera el valor independiente
			ss1=BYTE_TRANS(gen.ss1()) # signo solucion1
			ss2=BYTE_TRANS(gen.ss2()) # signo solucion2
			if b==0:
				if c==0:
					archivo.write(FORMAT('x^2=0').e());
				else:
					archivo.write(FORMAT('x^2'+signo2.Signo()+str(c)+'=0').e());
			elif b==1:
				if c==0:
					archivo.write(FORMAT('x^2'+signo1.Signo()+'x=0').e());
				else:
					archivo.write(FORMAT('x^2'+signo1.Signo()+'x'+signo2.Signo()+str(c)+'=0').e());
			else:
				if c==0:
					archivo.write(FORMAT('x^2'+signo1.Signo()+str(b)+'x=0').e());
				else:
					archivo.write(FORMAT('x^2'+signo1.Signo()+str(b)+'x'+signo2.Signo()+str(c)+'=0').e());
			print(ss1.Signo()+str(x1),ss2.Signo()+str(x2)) # imprime por consola las soluciones de la ecuación.
		archivo.write('\\end{enumerate}')
		archivo.close()
class ECU1(BYTE_TRANS,FORMAT):
	def __init__(self, r, nombre):
		self.r=r # La cantidad de ejercicios 'r'
		self.nombre=nombre # El nombre del archivo 'nombre'
	def Enunciado(self): # Modulo encargado de imprimir el enunciado para los ejercicios
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\section{Encontrar la solucion de:}');
		archivo.close()
	def Ejercicios(self): # Modulo encargado de imprimir en el archivo .tex los ejercicios
		archivo = open(str(self.nombre)+'.tex', 'a')
		archivo.write('\\begin{enumerate}');
		for f in range(1,self.r+1):
			terminos = []
			largo = random.randrange(3,6)
			igual = random.randrange(1,largo)
			# XXX aca se debe definir la letra aleatoria para que no se resetee
			for i in range(largo+2):
				if i == igual:
					terminos.append(['='])
				else: 
					termino=[]
					termino.append(BYTE_TRANS(random.randrange(2)).Signo()) # para signo
					termino.append(str(random.randrange(1,25))) # inserta en la tabla un numero aleatorio entre 1&25
					if i == 0: 
						termino.append('x')
						terminos.append(termino)
					elif i == largo+1:
						termino.append('')
						terminos.append(termino)
					else:
						termino.append(BYTE_TRANS(random.randrange(2)).Literal()) # para literal
						terminos.append(termino)
			primera=recorrersum(terminos,[])
			eliminar(primera,0,'+')
			eliminar(primera,primera.index('=')+1,'+')
			eliminarUNO(primera,'x')
			segunda=recorrersum(primera,'')
			archivo.write(FORMAT(segunda).e())
		archivo.write('\\end{enumerate}')
		archivo.close()
