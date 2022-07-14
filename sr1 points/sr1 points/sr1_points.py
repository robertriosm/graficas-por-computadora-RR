"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS
"""

from myrenderer import glCreateWindow, color

# resolution
width = 500
height = 500

# call object
render = glCreateWindow(width, height)
# set color and clear bg
render.glClearColor(0, 0, 0) # black
render.glClear()
# make viewport
render.glViewPort(width/10, height/10, width*0.8, height*0.8)
render.glClearViewport(color(0.3, 0.8, 0.1)) # cool green 
# draw normalized dots in the center and corners of the viewport
render.glNDCPoint(0, 0, color(1, 0, 0))
render.glNDCPoint(1, 1, color(1, 0, 0))
render.glNDCPoint(-1, -1, color(1, 0, 0))
render.glNDCPoint(0, 1, color(1, 0, 0))
render.glNDCPoint(0, -1, color(1, 0, 0))
# draw experimental vertex
render.glColor(0, 0, 1) # change color to blue
render.glVertex() # draw a sin and a log2
# write file
render.glFinish('image.bmp')