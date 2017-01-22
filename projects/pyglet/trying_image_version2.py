import pyglet

window=pyglet.window.Window()
image=pyglet.resource.image("index.jpeg")

#blitting at a different x,y coordinate
@window.event
def on_draw():
	window.clear()
	image.blit(90,90)

pyglet.app.run()
