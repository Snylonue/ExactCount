from numpy import sqrt
class tools(object):
	def __init__(self,l):
		self.list=l
	def count(self):
		s=1
		l=self.list
		for x in range(len(l)):
			l[x][0]=int((l[x][0]-l[x][0]%2)/2)
		print(l)
		for x in l:
			s=s*x[0]*x[1]
		return s
def isPrime(num):
	if (num==2 or num==3 or num==5 or num==7):
		return True
	elif (num<=1 or num%2==0 or num%3==0 or num%5==0 or num%7==0):
		return False
	else:
		max=int(sqrt(num))+1
	for x in range(3,max,2):
		#print(x)
		if (num%x==0):
			return False
		elif (x==max-1):
			return True
def inpoint(l,num,va=2):
	if (len(l)==0):
		return False,0
	else:
		for v,x in enumerate(l):
			if (x[va]==num):
				return True,v
			elif (v==len(l)-1):
				return False,0
def prime_factor(num):
	l=[num]
	while (not isPrime(l[-1]) and l[-1]!=1):
		print(l[-1])
		for x in range(2,l[-1]):
			if (l[-1]%x==0):
				l.insert(0,x)
				l[-1]=int(l[-1]/x)
				print(type(l[-1]))
			break
	return l
def number(l):
	if (len(l)==1):
		return 1
	else:
		s,sum_l=1,[]
		for x in range(len(l)-1):
			if (l[x]==l[x+1]):
				include,point=inpoint(sum_l,l[x],1)
				if (include):
					sum_l[point][0]+=1
				else:
					sum_l.append([2,l[x]])
		tool=tools(sum_l)
		return tool.count()
def simple(l):
	for v,x in enumerate(l):
		if (isPrime(x[2])):
			continue
		else:
			t=prime_factor(x[2])
			s=number(t)
			l[v][0]/=s
			s*=s
			l[v][0]/=s
	return l
def add_sqrt(l):
	l=simple(l)
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
def multiply_sqrt(l):
	s0,s1=1,1
	for x in l:
		s0*=x[0]
		s1*=x[2]
	return simple([s0,"sqrt",s1])

a=['6_sqrt_20','8_sqrt_15']
for x in range(len(a)):
	a[x]=a[x].split('_')
	a[x][0],a[x][2]=int(a[x][0]),int(a[x][2])
print(simple(a))
#print(isPrime(5))
#print(isPrime(7))
#print(prime_factor(20))