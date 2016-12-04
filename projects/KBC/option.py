import turtle as t 
def hex(opt,a,b):
	t.penup()
	t.setpos(a,b)
	t.pendown()
	t.color("green")
	t.begin_fill()
	t.left(60)
	t.fd(50)
	t.rt(60)
	t.fd(200)
	t.rt(60)
	t.fd(50)
	t.rt(60)
	t.fd(50)
	t.rt(60)
	t.fd(200)
	t.rt(60)
	t.fd(50)
	t.end_fill()
	t.penup()
	t.rt(120)
	t.fd(40)
	t.rt(90)
	t.fd(17)
	t.lt(90)
	t.pencolor("black")
	t.fd(20)
	t.write( opt, False, font=("Arial", 25, "bold"))
hex("ke",-250,-50)
hex("vi",250,-50)
hex("nn",-250,-150)
hex("klk",250,-150)








while True:
	t.position()
