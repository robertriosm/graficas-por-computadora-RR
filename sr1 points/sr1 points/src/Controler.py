"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS
"""

from src.Renderer import glCreateWindow, color, V2, V3, drawPolygon, Renderer
from Texture import Texture
from Shaders import flat, gourad

# resolution
width = 960
height = 540

rend = Renderer(width, height)

rend.active_shader = flat
rend.active_texture = Texture("models/Diffuse_2K.bmp")

rend.glLoadModel("models/Earth 2K.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 0, 0), 
                 scale = V3(30,30,30))

rend.glFinish("Ye.bmp")
