questions=["which os is most used in the world?", "Who is the writer of the harry potter series?", "Are you Mad?"]
options=[
		["A. linux", "B. windows", "C. mac", "D. iOS"],
		["A. Geronimo Stilton", "B. Roald Dahl", "C. Jeff Kinney", "D. J.K Rowling"],
		["Yes", "No"]
	]
answers=["A", "B", "YES"]
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

