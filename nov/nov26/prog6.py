l=[]
for x in range(3):
	num=int(raw_input())
	if num in l:
		print l
	else:
 		l.append(num)
		print l
