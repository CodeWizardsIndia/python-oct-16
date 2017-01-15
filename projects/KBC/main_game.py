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


def create_question(ques):
	margin=100
	w=t.window_width()
	ques_y=100
	ques_x= -w/2+ margin
	ques_color="#FF6600"
	ques_font=("arial",30,"normal")
	t.color(ques_color)
	t.penup()
	t.setx(ques_x)
	t.sety(ques_y)
	t.pendown()
	t.write(ques,False,font=ques_font)


def create_options(option_list):
	w=t.window_width()
	h=t.window_height()

	opt_w = 220
	x = (w/2 - opt_w)/2.0
	option(option_list[0],-x,-150)
	option(option_list[1],x+opt_w,-150)
	option(option_list[2],-x,-250)
	option(option_list[3],x+opt_w,-250)

def display_question_and_options(question_index):
	option_clicked = -1
	create_question(questions[question_index])
	option_list = options[question_index]
	create_options(option_list)

def get_option_index(x,y):
	global option_clicked, q_index
	if x<= -65 and x >= -262 and y >=-151 and y <= -64:
		option_clicked = 0
	elif x>= -265 and y>=-252 and x<=-63 and y<=-165:
		option_clicked = 2
	elif x<=335 and x>=135 and y<=-65 and y>=-152:
		option_clicked = 1
	elif x<=335 and x>=135 and y<=-165 and y>=-252:
		option_clicked = 3

	if option_clicked != -1:
		if option_clicked == answers[q_index]:
			print "you are right"
		else:
			print "you are wrong"
		option_clicked = -1
		q_index = q_index + 1
		for x in range(100):
			t.undo()
		display_question_and_options(q_index)


t.speed(0)
t.bgcolor("black")
t.bgpic("bg.png")
questions=["which os is most used in the world?", "Who is the writer of the harry potter series?", "Are you Mad?"]
options=[
                ["A. linux", "B. windows", "C. mac", "D. iOS"],
                ["A. Geronimo Stilton", "B. Roald Dahl", "C. Jeff Kinney", "D. J.K Rowling"],
                ["A. Yes", "B. No", "C. May be", "D. I don't know"]
        ]
answers=[0, 3, 0]

option_clicked = -1
q_index = 0

display_question_and_options(q_index)

t.onscreenclick(get_option_index)
t.mainloop()
