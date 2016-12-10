import turtle as t
def option(opt,x,y):
	t.color("#003366")
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.begin_fill()
	t.lt(60)
	t.fd(50)
	t.lt(60)
	t.fd(50)
	t.lt(60)
	t.fd(150)
	t.lt(60)
	t.fd(50)
	t.lt(60)
	t.fd(50)
	t.lt(60)
	t.fd(150)
	t.end_fill()
	t.color("#FF6600")
	t.penup()
	t.setpos(x-160,y+20)
	t.pendown()
	t.write(opt,False,font=("Arial",30,"bold"))

w=t.window_width()
h=t.window_height()

opt_w = 220
x = (w/2 - opt_w)/2.0

option("iOS",-x,-150)
option("linux",x+opt_w,-150)
option("Windows",-x,-250)
option("Android",x+opt_w,-250)
