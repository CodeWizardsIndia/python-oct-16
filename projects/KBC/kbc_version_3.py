import turtle as t


import logo
import options

t.speed(0)

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

option_clicked = -1
def get_option_index(x,y):
	if x<= -65 and x >= -262 and y >=-151 and y <= -64:
		option_clicked = 0
	elif x>= -265 and y>=-252 and x<=-63 and y<=-165:
		option_clicked = 2
	elif x<=335 and x>=135 and y<=-65 and y>=-152:
		option_clicked = 1
	elif x<=335 and x>=135 and y<=-165 and y>=-252:
		option_clicked = 3
	if option_clicked != -1:
		print option_clicked

t.onscreenclick(get_option_index)
t.mainloop()
