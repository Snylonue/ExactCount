#!/usr/bin/env python3

from math import gcd
from numpy import sqrt

class Number_tools(object):
	def notPrime(self,num):
		if (num<=1 or num%2==0 or num%3==0 or num%5==0 or num%7==0):
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
class Frac_processing(Number_tools):
	def simple_frac(self,l):
		for x,v in enumerate(l):
			m=gcd(v[0],v[2])
			v[0]//=m
			v[2]//=m
		return l
	def add_frac(self,l):
		l=self.simple_frac(l)
		s,s_l,lcm_l={},[],[]
		for x in l:
			if (x[2] in s):
				s[x[2]]+=x[0]
			else:
				s[x[2]]=x[0]
		for x in s:
			lcm_l.append(x)
		t=self.lcm(lcm_l)
		s_l.append([0,'frac',t])
		for x,v in s.items():
			s_l[0][0]+=v*(t//x)
		return self.simple_frac(s_l)
	def multiply_frac(self,l):
		s0,s1=1,1
		for x in l:
			s0*=x[0]
			s1*=x[2]
		return self.simple_frac([[s0,'frac',s1]])
	def devide_frac(self,l):
		for x,v in enumerate(l):
			if (x==0):
				continue
			else:
				v[0],v[2]=v[2],v[0]
		return self.multiply_frac(l)
class Root_processing(object):
	def simple_root(self,l):
		tool=Number_tools()
		for x,v in enumerate(l):
			if (type(v[2])==int):
				if (tool.isPrime(v[2])):
					continue
				else:
					t=tool.factor(v[2])
					s=number(t)
					l[x][0]*=s
					s*=s
					l[x][2]//=s
			else:
				pass
	def add_root(self,l):	
		l=simple_root(l)
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
		return simple_root([[s0,'sqrt',s1]])
	def devide_root(self,l):
		pass
