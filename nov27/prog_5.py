l = []

for x in range(10):
	u_n = int(raw_input("enter a number :"))
	l.append(u_n)

for y in l:
	if y%2==0:
		print "it is even"
	else:
		print "it is odd"
