#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import sqrt
from collections import deque,Counter

class Numtools(object):
	__max_cache=200000
	__factor_cache={}
	__primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139}
	__not_primes=set()
	@staticmethod
	def __notPrime(num):
		if any((num<=1,num%2 is 0,num%3 is 0,num%5 is 0,num%7 is 0,num%11 is 0,num%13 is 0,num%17 is 0,num%19 is 0)):
			return True
		else:
			return (num+1)%6!=0 and (num-1)%6!=0
	@classmethod
	def __set_factor_cache(cls,num,value:deque):
		if cls.__max_cache>len(cls.__factor_cache):
			cls.__factor_cache[num]=value
		return value
	@classmethod
	def isPrime(cls,num):
		if num in cls.__primes:
			return True
		elif num in cls.__not_primes or cls.__notPrime(num):
			return False
		else:
			end=int(sqrt(num))
			for x in range(11,end,7):
				if num%x is 0:
					if cls.__max_cache>len(cls.__not_primes):
						cls.__not_primes.add(num)
					return False
				elif x>=end-7:
					if cls.__max_cache>len(cls.__primes):
						cls.__primes.add(num)
					return True
			raise ValueError(f'Unknown error:number {num} has not finished judged')
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
class Itertools(object):
	@staticmethod
	def numgroups(iterable,n):
		result=[]
		for x,y in iterable,(i+1 for i in range(n)):
			if y%n==0:
				yield result
				result.clear()
			result.append(x)
		else:
			yield result
		