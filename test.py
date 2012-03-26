import pyglet
from random import uniform
from math import sqrt, pow

RANGE = 50

player = pyglet.media.Player()
player.queue(pyglet.media.load('sounds/107351__ermfilm__baby-crying-1-sounds-at-ermfilm-pl.wav', streaming=False))
#player.queue(pyglet.media.load('sounds/loop.wav', streaming=False))
player.eos_action = player.EOS_LOOP
player.position = (uniform(0,RANGE), uniform(0,RANGE), 0)
player.min_distance = 5.0
player.max_distance = 75.0
player.play()

# init some stuff
window = pyglet.window.Window()
key = pyglet.window.key
clock = pyglet.clock

# key events
@window.event
def on_key_press(symbol, modifiers):
    dx, dy = 0, 0
    if symbol == key.W:
        dy = 1
    elif symbol == key.A:
        dx = -1
    elif symbol == key.S:
        dy = -1
    elif symbol == key.D:
        dx = 1
    key_held(0, dx, dy)
    clock.schedule_interval(key_held, 0.15, dx, dy)

@window.event
def on_key_release(symbol, modifiers):
    clock.unschedule(key_held)

def key_held(dt, dx, dy):
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
