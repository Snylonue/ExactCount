import ExactCountR
t=ExactCountR.Root_processing()
#a,b=[[8,'root',[4,'frac',16]]],[[[4,'frac',19],'root',[3,'frac',14]]]
a=[[[4,19],3],[[3,20],5]]
a=ExactCountR.input_format(a)
o=t.devide_root(a)
print([[o.modu.mole,o.modu.deno],o.base])
#print(ExactCount.normal(a))
#print(ExactCount.normal(b))
#print(ExactCount.simple_root([[[1, 'frac', 2], 'root', 64]]))
#print(t.factor(64),t.factor(3**5))
#print(t.lcm([1,2,3,4,5]))