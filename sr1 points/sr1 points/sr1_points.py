"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS
LABORATORIO 1
"""

from myrenderer import glCreateWindow, color, V2

# resolution
width = 960
height = 540

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

def drawPoli(poligono, clr = None):
    for i in range(len(poligono)):
        render.glLine(poligono[i],
                    poligono[ (i + 1) % len(poligono)],
                    clr)

pol1 = [ V2(165, 380), V2(185, 360), V2(180, 330),
         V2(207, 345), V2(233, 330), V2(230, 360),
         V2(250, 380), V2(220, 385), V2(205, 410), V2(193, 383)]

pol2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

pol3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

pol4 = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53),
        V2(535, 36),  V2(676, 37),  V2(660, 52), V2(750, 145),
        V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214),
        V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214),
        V2(517, 144), V2(466, 180)]

pol5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

drawPoli(pol1, color(1,0.5,0.5))
drawPoli(pol2, color(0.5,1,0.5))
drawPoli(pol3, color(0.5,0.5,1))
drawPoli(pol4, color(1,1,1))
drawPoli(pol5, color(1,1,1))

# procedimiento para rellenar:
# recorrer la lista de vectores,
# ver un punto x1 que este mas a la izquierda y arriba,
# ver si tiene un punto x2 mas a la derecha para detenerse,
# hacer una linea recta desde x1 hasta x2,
# repetir asi hacia abajo hasta que se acabe el poligono
def fillPoli(poligono: list, clr = None):
    for i in range(len(poligono)):
        render.glLine(poligono[i],
            poligono[ (i - 1) % len(poligono)],
            clr)

# write file
render.glFinish('image.bmp')