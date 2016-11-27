list = []
for x in range(9):
	num =int(raw_input("enter any number"))
	if num in list:
		print "it is in the list"
	else:
		list.append(num)
		print list
