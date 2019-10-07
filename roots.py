#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numtools import *
from fractions import Fraction
from collections import defaultdict

class Root(Numtools):
	def __init__(self,modu=Fraction(),base=1):
		super().__init__()
		self.modu=modu
		self.base=base#need to check
		self.simple()
	def __str__(self):
		return f'Root({self.modu},{self.base})'
	def __add__(self,other):
		try:
			if self.base is other.base:
				return Root(self.modu+other.modu,self.base)
			else:
				return NotImplemented
		except ArithmeticError:
			return NotImplemented
	def __sub__(self,other):
		try:
			if self.base is other.base:
				return Root(self.modu-other.modu,self.base)
			else:
				return NotImplemented
		except ArithmeticError:
			return NotImplemented
	def __mul__(self,other):
		try:
			return Root(self.modu*other.modu,self.base*other.base)
		except ArithmeticError:
			return NotImplemented
	def __truediv__(self,other):
		try:
			return Root(self.modu/other.modu/other.base,self.base*other.base)
		except ArithmeticError:
			return NotImplemented
	def __pow__(self,num):
		res=Root(self.modu**num*self.base**(num//2))
		if num%2 is not 0:
			res.base=self.base
		return res
	def __count(self,l):
		if len(l) is 1:
			return 1
		else:
			s=defaultdict(lambda:1)
			for x,v in renumerate(l):
				s[v]+=1
			res=1
			for x,v in s.items():
				res*=x**(v//2)			
			return res
	def simple(self):
		if self.isPrime(self.base):
			pass
		else:
			m=self.__count(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	__repr__=__str__
