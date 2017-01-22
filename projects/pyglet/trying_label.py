import pyglet
window=pyglet.window.Window(width=530, height=620)

#this is my label
label=pyglet.text.Label("my text", font_name="arial", x=100, y=100)

# @window.event is decorator, we will study decorators in py102
@window.event
def on_draw():
	window.clear()
	label.draw()

#this is mainloop
pyglet.app.run()
