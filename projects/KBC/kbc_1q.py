import background
import turtle as t
import options

t.bgcolor("black")
margin = 175
w = t.window_width()
ques_y = 100
ques_x = -w/2 + margin
question_color = "grey"
question_font = ("arial","30","normal")
question = "Where is Taj Mahal situated ?"
t.color(question_color)
t.penup()
t.setx(ques_x)
t.sety(ques_y)
t.write(question , False , font = question_font)

def my_func(x,y):
	print x, y

	if x >= -333 and x <= -86 and y >= -192 and y <= -109:
		print "option 1 clicked"

t.onscreenclick(my_func)

t.mainloop()
