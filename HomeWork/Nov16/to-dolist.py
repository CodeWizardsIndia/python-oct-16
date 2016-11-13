#To Do List
print"To-Do List \n"
print "Day 1"
list1=['Grocery Shopping','Physics Class', 'Lunch With Friends' ,'Visit Family']
print "To Do List For Today =",list1
print"As Friends Have Emergencies, The Plan for",list1[2],"is cancelled"
del list1[2];
print"Instead I'll Go For A Game Of Squash!"
list1.insert(2,"Squash")
print "New To Do List",list1

print"\n Day 2"
list2=["Workout","College","Party"]
print list2
r=["Swimming","Football","Basketball"]
print "Help Me Decide What To Do In The Evening!"
print('''Type:
1. For Swimming.
2. For Football.
3. For Basketball''')
ch= input("Your Option: ")
if ch==1: 
    print"Your Choice is ",r[0]
    list2.insert(2,r[0])
    print "To Do List For Today is",list2
elif ch==2:
    print"Your Choice is ",r[1]
    list2.insert(2,r[1])
    print "To Do List For Today is",list2
elif ch==3:
    print"Your Choice is ",r[2]
    list2.insert(2,r[2])
    print "To Do List For Today is",list2
else:
    print"Invalid Input"
    print"If That Is The Case, I'll Sit At Home And Binge Watch!"
    list2.insert(2,"Binge Watching")
    print "To Do List For Today is",list2

    

    

