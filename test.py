import ExactCountR
t=ExactCountR.Root_processing()
#a,b=[[8,'root',[4,'frac',16]]],[[[4,'frac',19],'root',[3,'frac',14]]]

a=[[[3,1],5],[[2,1],[1,2]],[[-1,1],20],[[-1,2],32]]
a=ExactCountR.input_format(a)
print(a)
a=t.add_root(a)
for x in a:
	print([x.modu.mole,x.modu.deno],x.base)


