#!/usr/bin/env python3

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
		while (not self.isPrime(l[-1])):
			for x in range(2,l[-1]):
				if (l[-1]%x==0):
					l.insert(0,x)
					l[-1]//=x
					break
		return l
	def lcm(self,l):	#can be deleted
		slcm=lambda x,y:x//gcd(x,y)*y
		while (len(l)>1):
			t=(slcm(l[0],l[1]))
			l.pop(0)
			l[0]=t
		return l[0]
class Root(Number_tools):
	def __init__(self,modu=Fraction(),base=1):
		self.modu=modu
		self.base=base
	def simple(self):
		if (self.isPrime(self.base)):
			pass
		else:
			m=number(self.factor(self.base))
			self.modu*=m
			self.base//=m**2
	def frac_to_int(self):
		self.modu/=self.base.denominator
		self.base=self.base.numerator*self.base.denominator
class Root_processing(Number_tools):
	def add(self,l):
		s,re={},[]
		for x in l:
			x.simple()
			if (x.base in s):
				s[x.base]+=x.modu
			else:
				s[x.base]=x.modu
		for x,v in s.items():
			re.append(Root(v,x))
		return re
	def multiply(self,l):
		res=Root(Fraction(1,1),1)
		for x in l:
			res.modu*=x.modu
			res.base*=x.base
		res.simple()
		return res
	def devide(self,l):
		res=l[0]
		for x,v in enumerate(l):
			if (x==0):
				continue
			else:
				res.modu/=v.modu
				res.base/=v.base
		if (type(res.base)==Fraction):
			res.frac_to_int()
		res.simple()
		return res

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
