import pyglet
window=pyglet.window.Window(width=530, height=620)

#this is my label
label=pyglet.text.Label("my text", font_name="comic sans", font_size=40, x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

# @window.event is decorator, we will study decorators in py102
@window.event
def on_draw():
	window.clear()
	label.draw()

#this is mainloop
pyglet.app.run()
