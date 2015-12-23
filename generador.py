#! /usr/bin/env python
# -*- coding: utf-8 -*-
#generador de archivo

import os
from ecu import ECU2, ECU1
nombre = input('Ingrese nombre del archivo:')
sunombre= input('Ingrese su nombre:')

archivo = open(str(nombre)+'.tex', 'a')
print('Generando encabezado')
archivo.write('\\documentclass[11pt,a4paper]{article}\\usepackage[utf8]{inputenc}\\usepackage[T1]{fontenc}\\usepackage[spanish]{babel}\\usepackage{amsmath,amsfonts,amsthm}\\usepackage{parskip}\\usepackage[right=2cm,left=2cm,top=2cm,bottom=2cm,headsep=0cm,footskip=0.5cm]{geometry}\\title{\\textbf{Matemática}}\\author{'+str(sunombre)+'}\\date{}\\begin{document}\\maketitle\n');
archivo.close()
print('1)ecuaciones de segundo grado')
print('2)ecuaciones de primer grado')
ejercicios = int(input('tipo de ejercicios:'))
if ejercicios == 1:
	r=int(input('cuantos ejercicios:'))
	ecu2 = ECU2(r, nombre)
	ecu2.Enunciado()
	ecu2.Ejercicios()
elif ejercicios == 2:
	r=int(input('cuantos ejercicios:'))
	ecu1 = ECU1(r, nombre)
	ecu1.Enunciado()
	ecu1.Ejercicios()
else:
	print('fin')

archivo = open(str(nombre)+'.tex', 'a')
archivo.write("\\end{document}");
archivo.close()
pdf = os.popen('pdflatex '+nombre+'.tex').read()
limpieza1 = os.popen('rm '+nombre+'.log').read()
limpieza2 = os.popen('rm '+nombre+'.aux').read()
