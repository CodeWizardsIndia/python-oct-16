import pyglet
window = pyglet.window.Window(width=390, height=480)
#thisis my label
label =pyglet.text.Label("My text",font_name="arial",x=100,y=100)


#@window.event is a decorator, we will study decorators in py102
@window.event
def on_draw():
	window.clear()
	label.draw()
#this is mainloop
pyglet.app.run()
