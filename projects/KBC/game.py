questions = ["Which OS is most used in the world?","What is the capital of England?","Where is Taj Mahal located?" , "What is the capital of India?"]

options = [[ "A.  Linux", "B.  Windows", "C.  IOS" ] , ["A.  Delhi", "B.  London", "C.  Karachi", "D.  New York"] , ["A. Delhi" , "B. Agra" , "C. Chennai"] , ["A. New York" , "B. London" , "C. New Delhi"] ]

answers = [ "A", "B", "B", "C" ]
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
