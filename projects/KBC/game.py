questions = ["Which operating systym is most used in the world ?","what is the capital of england?"]
options = [
		["A. linux","B. windows","C. mac","D. ios"] ,
 		["A. dehli","B. london","C. karachi","D. new york"]
	  ]

answers = [ "A" , "B" ]

for ques in questions :

	print ques

	index = questions.index(ques)

	print "your options are:"

	print  options[index]
	
	real_answer = answers[index]

	user_answer = raw_input("enter your answer: ")

	user_answer = user_answer.upper()

	if  real_answer == user_answer:
		print "you are correct"
	else:
		print "you are wrong"
