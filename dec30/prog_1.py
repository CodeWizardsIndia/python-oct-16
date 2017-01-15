vowel = ["a","e","i","o","u"]
n = raw_input("enter a name")
num = 0
for c in n : 
	if c in vowel :
		num = num + 1
print num
