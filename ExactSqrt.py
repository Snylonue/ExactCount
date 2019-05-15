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
def simple(l):
	#
a=['6_sqrt_15','8_sqrt_15']
sum=add_sqrt(a)

print(sum)