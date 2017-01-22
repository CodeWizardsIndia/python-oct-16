import pyglet

window = pyglet.window.Window()

@window.event
def on_key_press(symbol,modifiers):
#	if symbol == pyglet.window.key.symbol:
	print "you pressed",symbol
pyglet.app.run()
