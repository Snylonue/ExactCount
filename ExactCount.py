import numpy
def check_prime(num):
	num=int(num)
	if (num==1):
		return False
	if (num==2):
		return True
	max=int(numpy.sqrt(num))+1
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
	while (check_prime(l[-1])==False and l[-1]!=1):
		for x in range(2,l[-1]):
			if (l[-1]%x==0):
				l.append(x)
				l[-1],l[-2]=int(l[-2]/l[-1]),l[-1]
				break
	return l
def double(l):
	for v,x in enumerate(l):
		if (x[0]%2==0):
			break
		else:
			l[v]-=1
	return l
def number(l):
	s,p,sum_l=[],-1,0
	for v,x in enumerate(l):
		if (v<=p):
			break
		num_x,n=1,1
		while (v+n<len(l) and l[v+n]==x):
			p=v+n
			num_x+=1
			n+=1
		s.append([num_x,x])
	for x in s:
		
	s=list(filter(lambda x:x[0]!=0,map(double,s)))
	for x in s:
		sum_l+=x[0]/2*x[1]
	return sum_l
def simple(l):
	for x in l:
		t=prime_factor(x[2])
		if (len(t)==1):
			break
		else:
			e=number(t)
			x[0]*=e
			x[2]/=e**2
	return l
def add_sqrt(l):
	sum_l=[]
	for v,x in enumerate(l):
		if (v!=0):
			include,point=inpoint(sum_l,x[2])	
			if (include):
				sum_l[point][0]+=x[0]
			else:
				sum_l.append([x[0],x[1],x[2]])
		else:
			sum_l.append([x[0],x[1],x[2]])
	return sum_l
#a=['6_sqrt_15','8_sqrt_15']
for x in range(len(a)):
	a[x][0],a[x][2]=int(a[x][0]),int(a[x][2])
#print(simple(a))

