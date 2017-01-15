#Take two strings from user and concat them, also join them with a space with three methods.
string_1 = raw_input("enter your name")
string_2 = raw_input("enter your surname")

#simple concat
print string_1 + string_2



#using join, joining with space
print " ".join([string_1, string_2])

#using only +
print string_1 + " " + string_2

