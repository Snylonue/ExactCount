#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd
from numpy import sqrt
from fractions import Fraction

class Number_tools(object):
	def __notPrime(self,num):
		if (type(num)!=int):
			return True
		elif (num<=1 or num%2==0 or num%3==0 or num%5==0 or num%7==0):
			return True
		elif ((num+1)%6!=0 and (num-1)%6!=0):
			return True
		elif (2**(num-1)%num!=1):
			return True
		else:
			return False
	def isPrime(self,num):
		if (num in [2,3,5,7,11,13,17,19]):
			return True
		elif (self.__notPrime(num)):
			return False
		else:
			max=int(numpy.sqrt(num))+1
			for x in range(11,max,2):
				if (num%x==0):
					return False
				elif (x>=num-7):
					return True
	def factor(self,num):
		l=[num]
		while (not self.isPrime(l[-1]) and l[-1]!=1):
			for x in range(2,l[-1]):
				if (l[-1]%x==0):
					l.insert(len(l)-1,x)
					l[-1]//=x
					break
		return l
class Root(Number_tools):
	def __init__(self,modu=Fraction(),base=1):
		self.modu=modu
		self.base=base
		self.simple()
	def __str__(self):
		return f'Root({self.modu},{self.base})'
	def __add__(self,selves):
		if (self.base==selves.base):
			return Root(self.modu+selves.modu,self.base)
	def __sub__(self,selves):
		if (self.base==selves.base):
			return Root(self.modu-selves.modu,self.base)
	def __mul__(self,selves):
		return Root(self.modu*selves.modu,self.base*selves.base)
	def __truediv__(self,selves):
		res_modu=self.modu/selves.modu/selves.base
		res_base=self.base*selves.base
		return Root(res_modu,res_base)
	def __pow__(self,num):
		self.modu**=num
		print(self.modu)
		self.modu*=self.base**(num//2)
		if (num%2==0):
			self.base=1
		return self
		#return Root(self.modu**num,)
	def simple(self):
		if (self.isPrime(self.base)):
			pass
		else:
			m=number(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	__repr__=__str__

def number(l):
	if (len(l)==1):
		return 1
	else:
		s={}	
		for x in range(len(l)-1):
			if (l[x]==l[x+1]):
				if (l[x] in s):
					s[l[x]]+=1
				else:
					s[l[x]]=2
		return count(s)
def count(d):
	s=1
	for x,v in d.items():
		v=(v-v%2)//2
		s*=x**v
	return s
def input_format(l):
	res=[]
	for x in l:
		x=Root(Fraction(x[0][0],x[0][1]),x[1])
		if (type(x.base)==list):
			x.base=Fraction(x.base[0],x.base[1])
			x.frac_to_int()
		res.append(x)
	return res
