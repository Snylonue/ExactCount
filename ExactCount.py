import numpy
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
		l.insert(0,l[-1])
		l.pop()
		return l
	def gcd(self,num1,num2):
		result=0
		if (num1>=num2):
			m,n=num1,num2
		else:
			m,n=num2,num1
		while (n!=0):
			m,n=n,n%m
			result=m
		return result
def count(d):
	s=1
	for x,v in d.items():
		d[x]=(v-v%2)//2
		s*=x*d[x]
	return s
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
def simple_root(l):
	tool=Number_tools()
	for x,v in enumerate(l):
		if (tool.isPrime(v[2])):
			continue
		else:
			t=tool.factor(v[2])
			s=number(t)
			l[x][0]*=s
			s*=s
			l[x][2]//=s
	return l
def simple_frac(l):
	pass
def add_sqrt(l):
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
def multiply_sqrt(l):
	s0,s1=1,1
	for x in l:
		s0*=x[0]
		s1*=x[2]
	return simple_root([[s0,'sqrt',s1]])
def add_frac(l):
	l=simple_frac(l)
	s,s_l={},[]
	for x in l:
		if (x[2] in s):
			s[x[2]]+=x[0]
		else:
			s[x[2]]=x[0]
	for x,v in s.items():
		s_l.append([v,'frac',x])
	return s_l
a=['6_sqrt_20','8_sqrt_80']
def multiply_frac(l):
	s0,s1=1,1
	for x in l:
		s0*=x[0]
		s1*=x[2]
	return simple([[s0,'frac',s1]])
for x in range(len(a)):
	a[x]=a[x].split('_')
	a[x][0],a[x][2]=int(a[x][0]),int(a[x][2])
t=Number_tools()
print(t.gcd(14,21))
input()