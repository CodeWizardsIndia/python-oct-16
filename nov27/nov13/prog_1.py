todo=[]
done=[]
for x in range (10000):
	print you have to do these tasks
	print todo
	print you have done these these tasks
	print done
	addtask=raw_input("type a task you want to add")
	todo.append(addtask)
	removetask=raw_input("If you have done a task then please enter it's exact name")
	todo.remove(removetask)
	done.append(removetask)

