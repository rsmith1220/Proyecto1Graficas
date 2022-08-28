#Rebecca Smith
#Seccion 20

from gl import Renderer, color, V2, V3
from textures import Texture
from obj import Obj
import random

from shaders import flat,unlit, gourad, toon, glow, textureBlend, sabor


w=700
h=700
z=-10

rend= Renderer(w,h)

rend.dirLight = V3(1,0,0)

# Chocolate chip cookie

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = sabor


# rend.glLoadModel("cookie.obj",
#                 translate = V3(-1, -1, -10),
#                 scale = V3(1,1,1),
#                 rotate = V3(0, -65, -90)
#                 )

# rend.active_texture = Texture("skin.bmp")
# rend.active_texture2 = Texture("normal.bmp")
# rend.active_shader = sabor

# # Oreo cookie
# rend.glLoadModel("oreo.obj",
#                 translate = V3(1, 1, -10),
#                 scale = V3(0.03,0.03,0.03),
#                 rotate = V3(0, -70, -90)
#                 )

# rend.active_texture = Texture("pan.bmp")
# rend.active_texture2 = Texture("pannormal.bmp")
# rend.active_shader = sabor


# # Crossiant bread
# rend.glLoadModel("bread.obj",
#                 translate = V3(1, -1.9, -10),
#                 scale = V3(0.5,0.5,0.5),
#                 rotate = V3(90, 0, 0)
#                 )


rend.active_texture = Texture("ceramic.bmp")
rend.active_texture2 = Texture("ceramicnormal.bmp")
rend.active_shader = sabor
# capuchino cup
rend.glLoadModel("cup.obj",
                translate = V3(0, 0, 0),
                scale = V3(0.001,0.001,0.001),
                rotate = V3(0, 0, 0)
                )

rend.glFinish("output.bmp")
