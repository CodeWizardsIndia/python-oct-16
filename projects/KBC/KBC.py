import turtle as t
import background
import options


t.bgcolor("black")
margin=100
w=t.window_width()
ques_y=100
ques_x= -w/2+ margin
ques_color="#FF6600"
ques_font=("arial",30,"normal")
ques="what is the most used OS?"
t.color(ques_color)
t.penup()
t.setx(ques_x)
t.sety(ques_y)
t.pendown()
t.write(ques,False,font=ques_font)

def my_print(x,y):
	print x, y

	if x<= -65 and x >= -262 and y >=-151 and y <= -64:
		print "you clicked iOS"
		
t.onscreenclick(my_print)


t.mainloop()
