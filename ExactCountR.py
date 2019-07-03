#!/usr/bin/env python3

#format:[[1,2],3],[[2,1],5]

from math import gcd
from numpy import sqrt

class Number_tools(object):
	def notPrime(self,num):
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
		elif (self.notPrime(num)):
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
	def lcm(self,l):
		slcm=lambda x,y:x//gcd(x,y)*y
		while (len(l)>1):
			t=(slcm(l[0],l[1]))
			l.pop(0)
			l[0]=t
		return l[0]
class Frac(Number_tools):
	def __init__(self,mole,deno):
		self.mole=mole
		self.deno=deno
	def simple_frac(self):
		m=gcd(self.mole,self.deno)
		self.mole//=m
		self.deno//=m
	def multiply_fracs(self,times):
		self.mole*=m
class Root(Number_tools):
	def __init__(self,modu,base):
		self.modu=modu
		self.base=base
	def simple_root(self):
		if (self.isPrime(self.base)):
			pass
		else:
			m=number(self.factor(self.modu))
			self.modu.multiply_fracs(m)
			self.modu.simple_frac()
			self.base//=m**2
class Frac_processing(Frac):
	def add_frac(self,l):
		t,r=set([]),[0,0]
		for x in l:
			t.add(x.deno)
		m=self.lcm(list(t))
		for x in l:
			r[0]+=m//x.deno*x.mole
			r[2]+=m
		re=Frac(r[0],r[2])
		re.simple_frac()
		return re
	def multiply_frac(self,l):
		s0,s1=1,1
		for x in l:
			s0*=x.mole
			s1*=x.deno
		re=Frac(s0,s1)
		re.simple_frac()
		return re
	def devide_frac(self,l):
		for x,v in enumerate(l):
			if (x==0):
				continue
			else:
				v.mole,v.deno=v.deno,v.mole
		return self.multiply_farc(l)
class Root_processing(Root):
	def add_root(self,l):	
		s,s_l={},[]
		for x in l:
			if (x[2] in s):
				s[x[2]]+=x[0]
			else:
				s[x[2]]=x[0]
		for x,v in s.items():
			s_l.append([v,'sqrt',x])
		return s_l
	def multiply_root(self,l):
		s0,s1=1,1
		for x in l:
			s0*=x[0]
			s1*=x[2]
		return self.simple_root([[s0,'sqrt',s1]])
	def devide_root(self,l):
		pass

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
	re=[]
	for x in l:
		if (True):
			re.append(Root(Frac(x[0][0],x[0][1]),x[1]))
		else:
			pass
	return re