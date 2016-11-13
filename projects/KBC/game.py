questions=["which os is most used in the world?", "what is the capital of England?"]
options=[
		["A. linux", "B. windows", "C. mac", "D. iOS"],
		["A. delhi", "B. london", "C. karachi", "D. newyork"]
	]
answers=["A", "B"]
for question in questions :
	print question
	index=questions.index(question)
	print "your options are:"
	print options[index]
	real_answer=answers[index]
	user_answer=raw_input("Enter Your Answer:")
	if real_answer ==user_answer.upper():
		print "your answer is correct"
	else:
		print "your answer is wrong"

