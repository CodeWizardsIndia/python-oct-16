import turtle as t
def sq(side,col):
	t.color(col)
	for x in range(4):
		t.fd(side)
		t.lt(90)

params = [[20,"red"], [30,"blue"], [25,"yellow"]]
for s,c in params:
	sq(s,c)


while True:
	t.pos
