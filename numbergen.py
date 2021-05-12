ctrl=0
while ctrl <= 100:
	ctrl+=1
	ctr2=1
	while ctr2<=(ctrl/2):
		ctr2+=1
		if(ctrl%ctr2) == 0:
			break
	else:
		print(ctrl)	