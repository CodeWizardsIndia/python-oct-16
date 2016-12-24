import turtle as t
questions = ["Which operating systym is most used in the world ?",
		"what is the capital of england?",
		"who is the Prime Minister of India?",
		"What is the capital of India" ,
		" The moon is a : ",
		"Who receives Dronacharya Award?",
                "Who was the first Indian to be-elected to the British Parliament?",
                " In which year India Joined the United Nations? ",
                " A hole is made in a brass plate and it is heated. The size of the hole will ",
                " Which language was patronised by the the rules of Delhi Sultanate? ",
                "Who discovered magnetic field of electric current? ",
                " Which country leads in the production of rubber? ",
                "Which is the most irrigated State in India?",
             ]
options = [
		["A. linux","B. windows","C. mac","D. ios"] ,
 		["A. delhi","B. london","C. karachi","D. new york"] ,
		["A. narender modi","B. parnab mukherji","C. rajiv gandhi", "D. sonia gandhi"] ,
		["A. dehli" , "B. karach" ," C. chennai" , "D. GOA" ] ,
		["A. COMET" ,"B. sattelite" , "C. star planet" , "D. planet"],
		["A. SCIENTEST" , "B. movie actors", "C. sports coaches", "D. sports men"] ,
                ["A. DADAbhai naroji" , "B. motilal nehru", "C. mahatma gandhi", "D. sonia gandhi"] ,
                ["A. 1954" , "B. 1955", "C. 1956", "D. 1957"] ,
                ["A. increase" , "B. decrese", "C.  first increase and then decrease", "D. remain unchanged"] ,
                ["A. hindi" , "B. arabic", "C. persian", "D. Turkish"] ,
                ["A. Ampere" , "B. faradey", "C. Fleming", "D. edison"] ,
                ["A. australia" , "B. india", "C. malaysia", "D.  Myanmar"] ,
                ["A. bihar" , "B. punjab", "C. andhra  Pradesh", "D. utter  Pradesh"]
	  ]
answers = [ "A" , "B" , "A" , "A" ,"B" ,"C" ,"A" , "B" , "C" ,  "B" , "C" , "C" , "A"]


def create_question(question):
	margin = 175
	w = t.window_width()
	ques_x = -w/2 + margin
	ques_y = 100
	question_color = "grey"
	question_font = ("arial","25","normal")
	t.bgcolor("black")
	t.color(question_color)
	t.penup()
	t.sety(ques_y)
	t.setx(ques_x)
	t.write(question , False ,font = question_font)

def opt(written,x,y):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        t.color("BLUE")
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
        t.pencolor("SKY BLUE")
        t.fd(20)
        t.write( written, False, font=("Arial", 25, "bold"))

t.bgpic("kbc logo.png")
t.bgcolor("black")

is_clicked = False
def is_option_clicked(x,y):
	print x, y
	global is_clicked
	if x >= -333 and x <= -86 and y >= -192 and y <= -109:
		print "option 1 clicked"
		is_clicked = True
		return
	if x >= 66 and x <= 317 and y >= -195 and y <= -108:
		print "option 2 clicked"
		is_clicked = True
		return
	if x >= -333 and x <= -84 and y >= -294 and y <= -208:
		print "option 3 clicked"
		is_clicked = True
		return
	if x >= 65 and x <= 315 and y >= -293 and y <= -208:
		print "option 4 clicked"
		is_clicked = True
		return
	is_clicked = False

w = t.window_width()
h = t.window_height()
opt_w = 270
x = (w/2 - opt_w)/2
left_x = -(x+opt_w)

number_of_questions = len(questions)
index = 0
while index < number_of_questions:
	question = questions[index]
	create_question(question)
	opt(options[index][0], left_x, -150)
	opt(options[index][1], x,      -150)
	opt(options[index][2], left_x, -250)
	opt(options[index][3], x,      -250)
	t.onscreenclick(is_option_clicked)
	if is_clicked:
		index = index+1
#t.mainloop()
