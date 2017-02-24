T=int(input())
for i in range(T):
	x,y,z=input().split()
	x=int(x)
	y=int(y)
	z=int(z)
	a=[x,y,z]
	a.sort()
	print (a[1])