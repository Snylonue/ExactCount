import ExactCountR
t=ExactCountR.Root_processing()
#a,b=[[8,'root',[4,'frac',16]]],[[[4,'frac',19],'root',[3,'frac',14]]]

a=[[[3,1],5],[[2,1],[1,2]],[[-1,1],20],[[-1,2],32]]
a=ExactCountR.input_format(a)
print(a)
a=t.add_root(a)
for x in a:
	print([x.modu.mole,x.modu.deno],x.base)

#print(ExactCount.normal(a))
#print(ExactCount.normal(b))
#print(ExactCount.simple_root([[[1, 'frac', 2], 'root', 64]]))
#print(t.factor(64),t.factor(3**5))
#print(t.lcm([1,2,3,4,5]))
#print(t.factor(119))