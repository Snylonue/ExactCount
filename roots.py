#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import sqrt,gcd
from fractions import Fraction
from collections import defaultdict,deque

class Numtools(object):
	__max_cache=1000
	__prime_cache={}
	__factor_cache={}
	__primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103}
	@staticmethod
	def __notPrime(num):
		if any((num<=1,num%2 is 0,num%3 is 0,num%5 is 0,num%7 is 0,num%11 is 0,num%13 is 0)):
			return True
		else:
			return (num+1)%6!=0 and (num-1)%6!=0
	@classmethod
	def __set_prime_cache(cls,num,value:bool):
		if cls.__max_cache>len(cls.__prime_cache):
			cls.__prime_cache[num]=value
		return value
	@classmethod
	def __set_factor_cache(cls,num,value:deque):
		if cls.__max_cache>len(cls.__factor_cache):
			cls.__factor_cache[num]=value
		return value
	@classmethod
	def isPrime(cls,num):
		if num in cls.__primes:
			return True
		elif cls.__notPrime(num):
			return False
		else:
			try:
				return cls.__prime_cache[num]
			except KeyError:
				end=int(sqrt(num))
				for x in range(11,end,7):
					if num%x is 0:
						return cls.__set_prime_cache(num,False) #return False
					elif x>=end-7:
						return cls.__set_prime_cache(num,True)  #return True
				raise ValueError(f'Unknown error:number {num} can not be judged')
	@classmethod
	def factor(cls,num):
		try:
			return cls.__factor_cache[num]
		except KeyError:
			l,last=deque([num]),num
			while last is not 1 and not cls.isPrime(last):	
				for x in range(2,last):
					if last%x==0:
						t=l.pop()
						l.append(x)
						l.append(t//x)
						break
				last=l[-1]		
			return cls.__set_factor_cache(num,l)
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
		if self.isPrime(self.base):
			pass
		else:
			m=self.__count(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	__repr__=__str__
