import turtle as t
t.bgcolor("black")
import background
import question
import options
def my_func(x,y):
	print x, y

	if x >= -333 and x <= -86 and y >= -192 and y <= -109:
		print "option 1 clicked"
	if x >= 66 and x <= 317 and y >= -195 and y <= -108:
		print "option 2 clicked"
	if x >= -333 and x <= -84 and y >= -294 and y <= -208:
		print "option 3 clicked"
	if x >= 65 and x <= 315 and y >= -293 and y <= -208:
		print "option 4 clicked"
t.onscreenclick(my_func)

t.mainloop()
