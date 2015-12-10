#! /usr/bin/env python
# -*- coding: utf-8 -*-

class BYTE_SIGNO():
	def __init__(self,s):
		self.s=s
	def Signo(self):
		if self.s==0:
			return '+'
		else:
			return '-'
