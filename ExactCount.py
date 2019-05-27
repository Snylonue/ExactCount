from numpy import sqrt
from functools import reduce
def check_prime(num):
	if (num==2 or num==3):
		return True
	if (num<=1 or num%2==0):
		return False
	if (num<9):
		max=num+1
	else:
		max=int(sqrt(num))+1
	for x in range(3,max,2):
		if (num%x==0):
			return False
		elif (x==max-1):
			return True
def inpoint(l,num,va=2):
	for v,x in enumerate(l):
		if (x[va]==num):
			return True,v
		elif (v==len(l)-1):
			return False,0
def prime_factor(num):
	l=[num]
	while (not check_prime(l[-1]) and l[-1]!=1):
		for x in range(2,l[-1]):
			if (l[-1]%x==0):
				l.append(x)
				l[-1],l[-2]=int(l[-2]/l[-1]),l[-1]
				break
	return l
def number(l):
	s,sum_l=[[1,1]],0
	for x in range(len(l)-2):
		if (l[x]==l[x+1]):
			include,point=inpoint(s,l[x],1)
			if (include):
				s[point][0]+=1
			else:
				s.append([2,l[x]])
	if (len(s)==1):
		return 1
	else:	
		s.pop(0)
		for v,x in enumerate(s):
			s[v][0]-=s[v][0]%2
		for x in s:
			sum_l+=x[0]/2*x[1]
		return int(sum_l)
def simple(l):
	for v,x in enumerate(l):
		e=number(prime_factor(x[2]))
		l[v][0]*=e
		l[v][2]/=e**2
	return l
def add_sqrt(l):
	s=[]
	for v,x in enumerate(l):
		if (v!=0):
			include,point=inpoint(sum_l,x[2])	
			if (include):
				s[point][0]+=x[0]
			else:
				s.append([x[0],x[1],x[2]])
		else:
			s.append([x[0],x[1],x[2]])
	return s
'''
a=['6_sqrt_20','8_sqrt_15']
for x in range(len(a)):
	a[x]=a[x].split('_')
	a[x][0],a[x][2]=int(a[x][0]),int(a[x][2])
'''
#print(check_prime(5))
#print(prime_factor(20))
