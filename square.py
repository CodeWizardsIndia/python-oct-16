import turtle as t

def square(j):
	t.fd(j)
	t.lt(90)
	t.fd(j)
	t.lt(90)
	t.fd(j)
	t.lt(90)
	t.fd(j)

z=int(raw_input())
square(z)
