#Rebecca Smith
#Seccion 20

from gl import Renderer, color, V2, V3
from textures import Texture
from obj import Obj
import random

from shaders import flat,unlit, gourad, toon, glow, textureBlend, sabor


w=800
h=800
z=-10

rend= Renderer(w,h)

rend.dirLight = V3(0,1,0)

# rend.background = Texture("plate.bmp")

# rend.glClearBackground()


# Chocolate chip cookie

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = sabor


rend.glLoadModel("cookie.obj",
                translate = V3(-2, -1, -10),
                scale = V3(0.7,0.7,0.7),
                rotate = V3(0, -65, -90)
                )

rend.active_texture = Texture("skin.bmp")
rend.active_texture2 = Texture("normal.bmp")
rend.active_shader = sabor

# Oreo cookie
rend.glLoadModel("oreo.obj",
                translate = V3(1, 1, -10),
                scale = V3(0.02,0.02,0.02),
                rotate = V3(0, -70, 90)
                )

rend.active_texture = Texture("pan.bmp")
# rend.active_texture2 = Texture("pannormal.bmp")
rend.active_shader = sabor


# Crossiant bread
rend.glLoadModel("bread.obj",
                translate = V3(1, -1.9, -10),
                scale = V3(0.5,0.5,0.5),
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
# Dona
# rend.active_texture = Texture("pandona.bmp")
# rend.active_texture2 = Texture("donasombra.bmp")
# rend.active_shader = toon

# rend.glLoadModel("dona.obj",
#                 translate = V3(1.1, 3, -10),
#                 scale = V3(20,20,20),
#                 rotate = V3(0, -90, -90)
#                 )

rend.glFinish("output.bmp")

