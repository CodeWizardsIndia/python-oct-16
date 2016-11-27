l = []
for x in range (10):
	a = int(raw_input("Enter a number: "))
	l.append(a)
for y in l:
	if y%2 ==0:
		print "The number is even"
	else:
		print "The number is odd" 
