import pyglet
from random import uniform
from math import sqrt, pow

RANGE = 50
player = pyglet.media.Player()
player.queue(pyglet.media.load('loop.wav', streaming=False))
player.eos_action = player.EOS_LOOP
player.position = (uniform(0,RANGE), uniform(0,RANGE), 0)
player.play()
print player.position
window = pyglet.window.Window()

@window.event
def on_mouse_motion(mouseX, mouseY, dx, dy):
    px, py, pz = player.position
    print player.position
    d = sqrt(pow(px,2) + pow(py,2))
    print 'dx:', dx, 'dy:', dy
    if d < 5:
        print 'win'
    newx = (px-dx) if abs(px-dx) < RANGE else px
    newy = (py-dy) if abs(py-dy) < RANGE else py
    player.position = newx, newy, pz

@window.event
def on_draw():
	window.clear()

pyglet.app.run()
