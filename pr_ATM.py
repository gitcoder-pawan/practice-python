x=list(map(float,input().split()))
if x[0]%5==0 and x[0]+.5<=x[1]:
	c=round(x[1]-x[0]-.5,2)
	print(c)
else:
	c=round(x[1],2)
	print(c)