import background
import turtle as t
margin=30
w=t.window_width()
ques_x= -w/2+ margin
ques_color="blue"
ques_font=("arial",18,"normal")
ques="what is the most used OS?"
t.color(ques_color)
t.penup()
t.setx(ques_x)
t.pendown()
t.write(ques,False,font=ques_font)
while True:
	t.position()
