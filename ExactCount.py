import numpy
def check_prime(num):
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
def inpoint(l,num):
	for v,x in enumerate(l):
		if (x[2]==num):
			return True,v
		elif (v==len(l)-1):
			return False,0
def prime_factor(num):
	l=[]
	l.append(num)
	while (check_prime(l[-1])==False and l[-1]!=1):
		for x in range(2,l[-1]):
			if (l[-1]%x==0):
				l.append(x)
				l[-1],l[-2]=int(l[-2]/l[-1]),l[-1]
				break
	return l
def simple(l):
	pass
def add_sqrt(l):
	sum=[]
	for v,x in enumerate(l):
		x[0],x[2]=int(x[0]),int(x[2])
		if (v!=0):
			include,point=inpoint(sum,x[2])	
			if (include):
				sum[point][0]+=x[0]
			else:
				sum.append([x[0],x[1],x[2]])
		else:
			sum.append([x[0],x[1],x[2]])
	return sum
a=['6_sqrt_15','8_sqrt_15']
for x in range(len(a)):
	a[x]=a[x].split('_')
print(add_sqrt(a))
