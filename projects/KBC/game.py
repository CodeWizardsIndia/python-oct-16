questions = ["Which OS is most used in the world?","What is the capital of England?"]

options = [[ "A.  Linux", "B.  Windows", "C.  IOS" ] , ["A.  Delhi", "B.  London", "C.  Karachi", "D.  New York"] ]

answers = [ "A", "B" ]
for  question in questions:
	print question
	index = questions.index(question)
	print "Your options are:"
	print options[index]
	real_answer = answers[index]
	user_answer = raw_input("Enter Your Answer: ")
	user_answer = user_answer.upper()
	if real_answer == user_answer :
		print "You are correct"
	else:
		print "You are wrong"  
