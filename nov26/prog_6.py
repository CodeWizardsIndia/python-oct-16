list = [4,56,67,23,54.89,45]
n = int(raw_input("enter any number"))
if n in list:
	print "yes"
else:
	list.append(n)
	print list
