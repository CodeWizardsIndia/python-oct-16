import turtle as t
t.bgpic("kbc logo.png")
margin = 15
w = t.window_width()
ques_x = -w/2 + margin
question_color = "blue"
question_font = ("arial","18","normal")
question = "Where is Taj Mahal situated ?"
t.color(question_color)
t.penup()
t.setx(ques_x)
t.write(question , False ,font = question_font) 
while True:
        t.position
def opt(written,x,y):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        t.color("yellow")
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
        t.pencolor("red")
        t.fd(20)
        t.write( written, False, font=("Arial", 25, "bold"))
opt("option 1",-350,-150)
opt("option 2",350,-150)
opt("option 3",-350,-250)
opt("option 4",350,-250)



