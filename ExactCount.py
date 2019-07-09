#!/usr/bin/env python3

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
	def simple(self):
		m=gcd(self.mole,self.deno)
		self.mole//=m
		self.deno//=m
class Root(Number_tools):
	def __init__(self,modu,base):
		self.modu=modu
		self.base=base
	def simple(self):
		if (self.isPrime(self.base)):
			pass
		else:
			m=number(self.factor(self.base))
			t=Frac(m,1)
			fp=Frac_processing()
			self.modu=fp.multiply_frac([t,self.modu])
			self.modu.simple()
			self.base//=m**2
class Frac_processing(Number_tools):
	def add_frac(self,l):
		t,r=set([]),[0,0]
		for x in l:
			t.add(x.deno)
		m=self.lcm(list(t))
		for x in l:
			r[0]+=m//x.deno*x.mole
			r[1]+=m
		re=Frac(r[0],r[1])
		re.simple()
		return re
	def multiply_frac(self,l):
		s0,s1=1,1
		for x in l:
			s0*=x.mole
			s1*=x.deno
		re=Frac(s0,s1)
		re.simple()
		return re
	def devide_frac(self,l):
		for x,v in enumerate(l):
			if (x==0):
				continue
			else:
				v.mole,v.deno=v.deno,v.mole
		return self.multiply_frac(l)
class Root_processing(Frac_processing):
	def add_root(self,l):
		s,re={},[]
		for x in l:
			x.simple()
			if (x.base in s):
				s[x.base]=self.add_frac([s[x.base],x.modu])
			else:
				s[x.base]=x.modu
		for x,v in s.items():
			re.append(Root(v,x))
		return re
	def multiply_root(self,l):
		modus,bases=[],1
		for x in l:
			modus.append(x.modu)
			bases*=x.base
		res_modus=self.devide_frac(modus)
		res=Root(res_modus,bases)
		res.simple()
		return res
	def devide_root(self,l):
		modus,s_temp=[],1
		for x in l:                #处理系数
			modus.append(x.modu)
		res_modus=self.devide_frac(modus)
		for x,v in enumerate(l):
			if (x==0):
				continue
			else:
				s_temp*=v.base
		res=Root(Frac(1,s_temp),l[0].base*s_temp)
		res.modu=self.multiply_frac([res.modu,res_modus])
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
	re=[]
	for x in l:
		if (type(x[1])==list):
			t=gcd(x[1][0],x[1][1])
			x[1][0]//=t
			x[1][1]//=t
			x[0][1]*=x[1][1]
			x[1]=x[1][0]*x[1][1]
		re.append(Root(Frac(x[0][0],x[0][1]),x[1]))
	return re
