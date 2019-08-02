#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd
from numpy import sqrt
from fractions import Fraction
from collections import defaultdict,deque

class Numtools(object):
	__instance=None
	def __new__(cls,*args,**kwargs):
		if cls.__instance is None:
			cls.__instance=object.__new__(cls)
		return cls.__instance
	def __init__(self):
		self.__max_cache=500000
		self.__cache=defaultdict(lambda:2)
	def __notPrime(self,num):
		if (type(num)!=int):
			return True
		elif (num<=1 or num%2==0 or num%3==0 or num%5==0 or num%7==0):
			return True
		elif ((num+1)%6!=0 and (num-1)%6!=0):
			return True
		else:
			return False
	def isPrime(self,num):
		if (num in [2,3,5,7,11,13,17,19]):
			return True
		elif (self.__notPrime(num)):
			return False
		else: 
			cache=self.__cache[num]
			if cache is 2:
				end=sqrt(num)
				not_cache_full=len(self.__cache)<self.__max_cache
				for x in range(11,num,7):
					if (num%x is 0):
						if not_cache_full:
							self.__cache[num]=0
						return False
					elif (x>=end):
						if not_cache_full:
							self.__cache[num]=1
						return True
			else:
				return bool(cache)
	def factor(self,num):
		l=deque([num])
		while (num!=1 and not self.isPrime(num)):
			for x in range(2,num):
				if (num%x==0):
					t=l.pop()
					l.append(x)
					l.append(t//x)
					break
			num=l[-1]
		return l
class Root(Numtools):
	def __init__(self,modu=Fraction(),base=1):
		self.modu=modu
		self.base=base
		self.simple()
	def __str__(self):
		return f'Root({self.modu},{self.base})'
	def __add__(self,self2):
		if (self.base==self2.base):
			return Root(self.modu+self2.modu,self.base)
	def __sub__(self,self2):
		if (self.base==self2.base):
			return Root(self.modu-self2.modu,self.base)
	def __mul__(self,self2):
		return Root(self.modu*self2.modu,self.base*self2.base)
	def __truediv__(self,self2):
		self.modu/=self2.modu/self2.base
		self.base*=self2.base
		return self
	def __pow__(self,num):
		self.modu**=num
		print(self.modu)
		self.modu*=self.base**(num//2)
		if (num%2==0):
			self.base=1
		return self
		#return Root(self.modu**num,)
	def __count(self,l):
		if (len(l)==1):
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
		if (self.isPrime(self.base)):
			pass
		else:
			m=self.__count(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	__repr__=__str__


'''
here's old code
def input_format(l): 
	res=[]
	for x in l:
		x=Root(Fraction(x[0][0],x[0][1]),x[1])
		if (type(x.base)==list):
			x.base=Fraction(x.base[0],x.base[1])
			x.frac_to_int()
		res.append(x)
	return res
'''
