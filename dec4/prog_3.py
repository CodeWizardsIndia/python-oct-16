import turtle as t
def square (side,col):
	t.color(col)
	t.begin_fill()
	for x in range(4):
		t.fd(side)
		t.lt(90)
	t.end_fill()
s = int(raw_input("enter the side of the square"))
c = raw_input("enter the color of square")
square(s,c)
