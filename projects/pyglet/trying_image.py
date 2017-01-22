import pyglet 
window=pyglet.window.Window(fullscreen=True)
image=pyglet.resource.image("image.jpg")
@window.event
def on_draw():
	window.clear
	image.blit(0,0)
pyglet.app.run()
