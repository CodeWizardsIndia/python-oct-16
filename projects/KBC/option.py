import turtle as t
t.penup()
t.setpos(-350,-150)
t.pendown()
t.color("red")
t.begin_fill()
t.fd(200)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(200)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)
t.end_fill()
t.penup()
t.pencolor("yellow")
t.lt(90)
t.fd(50)
t.pendown()
t.write("Option 1",False,font=("arial",20,"bold"))
while True:
	t.pos()
