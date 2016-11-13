questions = ["Which OS is most used in the world? ",
		"What is the capital of England?"]

options = [
		["A: Linux","B: Windows","C: Mac","D: IOS"],
		["A: London","B: Oxford","C: Manchester","D: Leeds"]


	]


answers=["A","A"]

for ques in questions:
	print ques
	index= questions.index(ques)
	print "Your Options Are:"
	print options[index]

	real_ans= answers[index]
	user_ans= raw_input("Enter Your Option: ")
	user_ans=user_ans.upper()
	if real_ans==user_ans:
		print"You are Correct"
	else:
		print"You are wrong"
