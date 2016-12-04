import turtle as t

def sq (n,col):
	t.color(col)
	t.begin_fill()
	for y in range(4):
		t.fd(n)
		t.lt(90)
	t.end_fill()

def sq5 (m, col):
	for x in range(1,6,1):
		sq(m*x, col)

s = int(raw_input("enter the side of the sq."))
c = raw_input("enter color")

sq5(s, c)
