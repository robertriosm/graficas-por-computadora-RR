"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
PROGRAMA PRINCIPAL PARA CONTROLAR LA LIBRERIA DE GRAFICAS
LABORATORIO 1
"""

from myrenderer import glCreateWindow, color, V2, drawPolygon #, drawStar

# resolution
width = 700
height = 600

# call object
render = glCreateWindow(width, height)
# set color and clear bg
render.glClearColor(0, 0, 0) # black
render.glClear()
render.glColor(1, 1, 1) # change color to blue
"""
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

drawPolygon(pol1, color(1,0.5,0.5))
drawPolygon(pol2, color(0.5,1,0.5))
drawPolygon(pol3, color(0.5,0.5,1))
drawPolygon(pol4, color(1,1,1))
drawPolygon(pol5, color(1,1,1))

# procedimiento para rellenar:
# recorrer la lista de vectores,
# ver un punto x1 que este mas a la izquierda y arriba,
# ver si tiene un punto x2 mas a la derecha para detenerse,
# hacer una linea recta desde x1 hasta x2,
# repetir asi hacia abajo hasta que se acabe el poligono
#def fillPoli(poligono: list, clr = None):
#    for i in range(len(poligono)):
#        render.glLine(poligono[i],
#            poligono[ (i - 1) % len(poligono)],
#            clr)


xxxtentacion = [V2(265, 380), V2(215, 430), 
                V2(265, 380), V2(315, 430), 
                V2(265, 380), V2(215, 330),
                V2(265, 280), V2(215, 230),
                V2(165, 280), V2(215, 180),
                V2(165, 280), V2(215, 330)]

# lineas de esquina a esquina
for x in range(width):
    if x % 10 == 0:
        render.glLine(V2(x, 0), V2(width, x), color((x/500)*.8, (x/500)*.5, x/500))
        render.glLine(V2(0, x), V2(x, width), color((x/500)*.5, (x/500), (x/500)*.8))

"""        

# polygons vectors

x = [
        V2(200, 200), V2(250, 250), V2(300, 200), V2(350, 250), V2(400, 200),
        V2(350, 150), V2(400, 100), V2(350, 50), V2(300, 100), V2(250, 50), 
        V2(200, 100), V2(250, 150)
    ]

star = [
            V2(500, 140), 
            V2(540, 140), 
            V2(550, 100), 
            V2(560, 140), 
            V2(600, 140),
            V2(570, 160), 
            V2(580, 200), 
            V2(550, 180), 
            V2(520, 200), 
            V2(530, 160)
       ]

house = [
            V2(100, 300),
            V2(250, 300),
            V2(250, 400),
            V2(300, 400),
            V2(175, 450),
            V2(50, 400),
            V2(100, 400)
        ]

man = [
        V2(540, 250), 
        V2(550, 250), 
        V2(550, 270), 
        V2(560, 270), 
        V2(560, 250), 
        V2(570, 250), 
        V2(570, 290), 
        V2(590, 290), 
        V2(590, 300), 
        V2(560, 300), 
        V2(560, 310), 
        V2(550, 310), 
        V2(550, 300),
        V2(520, 300), 
        V2(520, 290), 
        V2(540, 290)
      ]

rombo = [
        V2(400, 370), 
        V2(450, 400), 
        V2(450, 450), 
        V2(400, 480), 
        V2(350, 450), 
        V2(350, 400)
      ]

# draw them
drawPolygon(x, render, color(0.1,0.5,1))
drawPolygon(star, render, color(0.3,0.7,1))
drawPolygon(house, render, color(0.8,0.3,1))
drawPolygon(man, render, color(0.9,0.1,1))
drawPolygon(rombo, render, color(0.4,0.3,1))


# write file
render.glFinish('image.bmp')