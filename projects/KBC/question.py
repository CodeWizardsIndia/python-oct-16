import background
import turtle as t
import option

margin =175
w = t.window_width()
question_x = -w/2 + margin
question_color = "black"
question_font = ("Arial", 26, "bold")
question = "What is the capital of India? "
t.color(question_color)
t.penup()
t.setx(question_x)
t.pendown()
t.write(question, False, font = question_font)

def my_print(x,y):
	if x <= -83  and x >= -335 and y<= -90 and y>= -175:
		print "You Clicked Option 1"
	elif x >= -66 and x <= 316 and y<= -90 and y>= -175:
		print "You Clicked Option 2"
	elif x <= -83 and x >= -335 and y<= -190 and y>= -275:
		print "You Clicked Option 3"
	elif x >= 66 and x <= 316 and y<= -190 and y>=-275:
		print "You Clicked Option 4"
t.onscreenclick(my_print)

t.mainloop()
