import pyglet # import the library
win= pyglet.window.Window() # create the window
import util
from colorama import Fore, Back, Style
from tkinter import *


keys = pyglet.window.key.KeyStateHandler()
win.push_handlers(keys)

print(Fore.GREEN)
print(Style.NORMAL)


img1= pyglet.image.load('Legacy/PNG/roadTile11.png')
spr1 = pyglet.sprite.Sprite(img1, x = 0, y = 0)


img= pyglet.image.load('isometric_vehicles/green_vehicles.png')
img = img.get_region(x=96, y=0, width=32, height=32)
spr = pyglet.sprite.Sprite(img, x = 200, y = 200)
spr.scale = 3


# Start the event loop
def update(dt):  
     win.clear()


     if keys[pyglet.window.key.LEFT]:
      spr.x -= 2
     if keys[pyglet.window.key.RIGHT]:
      spr.x += 2
     if keys[pyglet.window.key.UP]:
      spr.y += 2
     if keys[pyglet.window.key.DOWN]:
       spr.y -=2

@win.event
def on_draw():
    win.clear()
    util.pixelScale()
    spr.draw()
    spr1.draw()
    




pyglet.clock.schedule(update) 
pyglet.app.run() 
