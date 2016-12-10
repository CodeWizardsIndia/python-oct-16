import turtle as t 
def hex(opt,a,b):
	t.penup()
	t.setpos(a,b)
	t.pendown()
	t.color("#89DA59")
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
	t.penup()
	t.setpos(0,0)
	t.pendown()
w = t.window_width()
h = t.window_height()

hex_w= 270
x = (w/2.0-hex_w)/2


hex("Option 1",-(hex_w+x),-130)
hex("Option 2",x,-130)
hex("Option 3",-(hex_w+x),-230)
hex("Option 4",x,-230)


