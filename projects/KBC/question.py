import background
import turtle as t
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
