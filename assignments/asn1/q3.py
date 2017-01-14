#Print negative, zero or positive if a number is <0 , ==0 or >0 respectivey, take number from user.
def no(a):
	if a<0:
		print "negative"
	elif a>0:
		print "positive"
	else:
		print "it is zero"
a=int(raw_input("enter no."))
no(a)
