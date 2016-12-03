import background
import turtle as t
margin = 25
w = t.window_width()
question_x = -w/2 + margin
question_color = "red"
question_font = ("Arial", 18, "bold")
question = "What is the capital of India? "
t.color(question_color)
t.penup()
t.setx(question_x)
t.pendown()
t.write(question, False, font = question_font)
while  True:
	t.position()
