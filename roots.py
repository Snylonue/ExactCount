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
		self.__prime_cache=defaultdict(lambda:2)
		self.__factor_cache=defaultdict(lambda:deque([]))
	def __notPrime(self,num):
		if num<=1 or num%2 is 0 or num%3 is 0 or num%5 is 0 or num%7 is 0:
			return True
		elif (num+1)%6!=0 and (num-1)%6!=0:
			return True
		else:
			return False
	def isPrime(self,num):
		if num in (2,3,5,7,11,13,17,19):
			return True
		elif self.__notPrime(num):
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
		if len(self.__factor_cache[num]) is not 0:
			return self.__factor_cache[num]
		l=deque([num])
		while num is not 1 and not self.isPrime(num):
			print(l)
			for x in range(2,num):
				if (num%x==0):
					t=l.pop()
					l.append(x)
					l.append(t//x)
					break
			num=l[-1]
		self.__factor_cache[num]=l
		return l
class Root(Numtools):
	def __init__(self,modu=Fraction(),base=1):
		super().__init__()
		self.modu=modu
		self.base=base#need to check
		self.simple()
	def __str__(self):
		return f'Root({self.modu},{self.base})'
	def __add__(self,self2):
		if self.base is self2.base:#haven't finished
			return Root(self.modu+self2.modu,self.base)
	def __sub__(self,self2):
		if self.base is self2.base:#haven't finished
			return Root(self.modu-self2.modu,self.base)
	def __mul__(self,self2):
		return Root(self.modu*self2.modu,self.base*self2.base)
	def __truediv__(self,self2):
		return Root(self.modu/self2.modu/self2.base,self.base*self2.base)
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
		if (self.isPrime(self.base)):
			pass
		else:
			m=self.__count(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	__repr__=__str__
