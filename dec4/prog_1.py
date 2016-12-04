import turtle as t
def square (col,s):
	t.color(col)
	for x in range(4):
		t.fd(s)
		t.lt(90)
sd = int(raw_input("enter the side of the square"))
c = raw_input("enter the color of the square")
square(c, sd)
while true:
	t.pos()
