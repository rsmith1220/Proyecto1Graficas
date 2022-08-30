#Rebecca Smith
#Seccion 20

from gl import Renderer, color, V2, V3
from textures import Texture
from obj import Obj
import random

from shaders import flat,unlit, gourad, toon, glow, textureBlend, sabor, normalMap


w=1300
h=866
z=-10

rend= Renderer(w,h)

rend.dirLight = V3(0,1,0)

rend.background = Texture("platito.bmp")

rend.glClearBackground()


# Chocolate chip cookie

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = normalMap


rend.glLoadModel("cookie.obj",
                translate = V3(-1, 1, -10),
                scale = V3(0.6,0.6,0.6),
                rotate = V3(0, -65, -90)
                )

rend.active_texture = Texture("skin.bmp")
rend.active_texture2 = Texture("normal.bmp")
rend.active_shader = sabor

# Oreo cookie
rend.glLoadModel("oreo.obj",
                translate = V3(1.5, 1, -10),
                scale = V3(0.02,0.02,0.02),
                rotate = V3(0, -70, 90)
                )

rend.active_texture = Texture("pan.bmp")
# rend.active_texture2 = Texture("pannormal.bmp")
rend.active_shader = sabor


# Crossiant bread
rend.glLoadModel("bread.obj",
                translate = V3(1, -1.6, -10),
                scale = V3(0.4,0.4,0.4),
                rotate = V3(90, 0, 0)
                )


rend.active_texture = Texture("ceramic.bmp")
rend.active_texture2 = Texture("ceramicnormal.bmp")
rend.active_shader = gourad
# coffee cup

rend.glLoadModel("cupa.obj",
                translate = V3(-1.1, 4, -10),
                scale = V3(0.6,0.6,0.6),
                rotate = V3(0, -90, -90)
                )


# Banana
rend.active_texture = Texture("banana.bmp")
# rend.active_texture2 = Texture("donasombra.bmp")
rend.active_shader = flat

rend.glLoadModel("banana.obj",
                translate = V3(6, 1, -10),
                scale = V3(20,20,20),
                rotate = V3(0, -180, -90)
                )

rend.glFinish("output.bmp")

