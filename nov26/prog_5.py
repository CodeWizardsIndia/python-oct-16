my_list = [1,2,3,4,5,6,7,8,9]
num = int(raw_input("Enter a number: "))
if num in my_list: 
	print my_list
else: 
	my_list.append(num)
	print my_list
