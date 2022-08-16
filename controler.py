"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS


from gl import Renderer, V3
from texture import Texture
from shaders import flat
import os

width = 540
height = 540

rend = Renderer(width, height)
 
rend.active_shader = flat
rend.active_texture = Texture("models/paper.bmp")

file_path = os.startfile("C://sr1 points")

rend.glLoadModel("models/gatito.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 0, 0), 
                 scale = V3(40,40,40))

rend.glFinish("gatito.bmp")
""" 

import os 

print(os.listdir("./models"))