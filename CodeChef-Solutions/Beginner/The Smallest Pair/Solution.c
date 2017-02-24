t=int(input())
for i in range(t):
	n=int(input())
	a=input().split(' ')
	l=[]
	l=list(a)
	c=[]
	c=sorted(l)
	print(int(c[0])+int(c[1]))