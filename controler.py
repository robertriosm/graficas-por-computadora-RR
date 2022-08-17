"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS
"""

from gl import Renderer, V3
from texture import Texture
from shaders import flat

width = 2000
height = 1000

rend = Renderer(width, height)
 
rend.active_shader = flat
rend.active_texture = Texture("models/marmol.bmp")

# golem
rend.glLoadModel("models/Stone.obj",
                 translate = V3(100, height/2 + 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glLoadModel("models/Stone.obj",
                 translate = V3(width/3 + 100, height/2 + 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glLoadModel("models/Stone.obj",
                 translate = V3((2*width)/3 + 100, height/2 + 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glLoadModel("models/Stone.obj",
                 translate = V3(100, 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glLoadModel("models/Stone.obj",
                 translate = V3(width/3 + 100, 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glLoadModel("models/Stone.obj",
                 translate = V3((2*width)/3 + 100, 100, 0),
                 rotate = V3(0, 0, 0),
                 scale = V3(20,20,20))

rend.glFinish("golemye.bmp")