import pyglet 
window=pyglet.window.Window(fullscreen=True)
image=pyglet.resource.image("image.jpg")
@window.event
#blitting at a different x y coorinate
def on_draw():
	window.clear
	image.blit(180,180)
pyglet.app.run()
