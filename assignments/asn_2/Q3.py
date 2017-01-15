#Take a string from user and print 1 character from starting to end per new line.
str = str(raw_input("enter a word"))
l = len(str)
for x in range(l):
	print str[x]
