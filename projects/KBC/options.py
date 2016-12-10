import turtle as t
def opt(written,x,y):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        t.color("BLUE")
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
        t.pencolor("SKY BLUE")
        t.fd(20)
        t.write( written, False, font=("Arial", 25, "bold"))
w = t.window_width()
h = t.window_height()

opt_w = 270
x = (w/2 - opt_w)/2

left_x = -(x+opt_w)

opt("DEHLI",left_x,-150)
opt("AGRA",x,-150)
opt("MATHURA",left_x,-250)
opt("GOA",x,-250)


