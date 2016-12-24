import turtle as t
def create_question(question):
	margin = 175
	w = t.window_width()
	ques_x = -w/2 + margin
	ques_y = 100
	question_color = "grey"
	question_font = ("arial","25","normal")
	t.color(question_color)
	t.penup()
	t.sety(ques_y)
	t.setx(ques_x)
	t.write(question , False ,font = question_font)
