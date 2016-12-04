def odd_even(a,b,c):
	l = [a,b,c]
	for x in l:
		if x%2 == 0:
			print("The number is even: ")
		else:
			print("The number is odd ")
x = int(raw_input("Enter a no. "))
y = int(raw_input("Enter a no. "))
z = int(raw_input("Enter a no. "))
odd_even(x,y,z)
