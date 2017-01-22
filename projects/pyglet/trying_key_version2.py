import pyglet

w = pyglet.window.Window()

@w.event
def on_key_press(symbol, modifiers):
	if symbol == pyglet.window.key.V:
		print "you pressed ", symbol

pyglet.app.run()
