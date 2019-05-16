import numpy
def include(l,num):
	if (l==[]):
		return False
	for x in range(len(l)-1):
		if (l[x]==num):
			return True
		elif (x==len(l)-1):
			return False
def point(l,num):
	for x in range(len(l)-1):
		if (l[x][1]==num):
			return x
def add_sqrt(l):
	s=[]
	for x in range(1,len(l)):
		t=l[x].split('_')
		t[0],t[2]=int(t[0]),int(t[2])
		if (include(s,t[2])):
			p=point(s,t[2])
			s[p][0]+=t[0]
		else:
			s.append([t[0],t[2]])
		#s=
	return s
def check_prime(num):
	t=2
	max=int(numpy.sqrt(num))
	if (num<=0 or num==1 or num%2==0):
		return False
	elif (num==3):
		return True
	else:
		while (t<=max):
			if (num%t==0):
				return False
			elif (t==max):
				return True
			else:
				t+=1
def f_temp(num):
	l=[]
	l.append(num)
	while (check_prime(l[-1])==False):
		for x in range(2,l[-1]):
			if (l[-1]%x==0):
				l.append(x)
				l[-1],l[-2]=int(l[-2]/l[-1]),l[-1]
				break
	return l
def simple(l):
	pass
