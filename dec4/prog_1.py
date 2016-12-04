import turtle as t
def sq(side, color):
	t.color(color)
	t.begin_fill()
	for x in range (4):
		t.fd(side)
		t.lt(90)
	t.end_fill()
for x in range (3):
	s = int(raw_input("Please enter a number: "))
	c = raw_input("Please enter your color: ")
	sq(s,c)
while True: 
	t.pos()
