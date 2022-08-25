
# controlador para ejecutar el lab

from gl import Renderer, color, V2
import sys
sys.setrecursionlimit(500000)
width = 800
height = 500

rend = Renderer(width, height)
colorbordeado = (1, 0.4, 0.4)
colorrelleno = (0.5, 0.9, 0.7)
rend.glColor(1, 0.4, 0.4)

def drawListOfPoints(Posiciones):
    for i in range(len(Posiciones)):
        if i == len(Posiciones)-1:
            rend.glLine(Posiciones[0], Posiciones[i])
            break
        rend.glLine(Posiciones[i], Posiciones[i+1])

def boundaryFillin(x, y, colorBordes, colorRelleno):
    pixel_color = rend.getPixel(x, y)
    colorBordes = color(1, 0.4, 0.4)
    colorRelleno = color(0.5, 0.9, 0.7)
    if pixel_color != colorBordes and pixel_color != colorRelleno:
        rend.glPoint(x, y, colorRelleno)
        boundaryFillin(x + 1, y, colorBordes, colorRelleno)
        boundaryFillin(x - 1, y, colorBordes, colorRelleno)
        boundaryFillin(x, y + 1, colorBordes, colorRelleno)
        boundaryFillin(x, y - 1, colorBordes, colorRelleno)

def boundaryFillinALT(x, y, colorBordes, colorRelleno):
    pixel_color = rend.getPixel(x, y)
    colorBordes = color(1, 0.4, 0.4)
    colorRelleno = color(0.5, 0.9, 0.7)
    if pixel_color != colorBordes and pixel_color != colorRelleno:
        rend.glPoint(x, y, colorRelleno)
        rend.glFinish("output.bmp")
        boundaryFillinALT(x + 1, y, colorBordes, colorRelleno)
        boundaryFillinALT(x, y + 1, colorBordes, colorRelleno)
        boundaryFillinALT(x - 1, y, colorBordes, colorRelleno)
        boundaryFillinALT(x, y - 1, colorBordes, colorRelleno)


#Poligono 1
poligono1 = [ V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345), 
                V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385),
                V2(205, 410), V2(193, 383)]
drawListOfPoints(poligono1)
boundaryFillin(180, 380, colorbordeado, colorrelleno)


#Poligono 2
poligono2 = [ V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]
drawListOfPoints(poligono2)
boundaryFillin(321, 334, colorbordeado, colorrelleno)

#Poligono 3
poligono3 = [ V2(377, 249), V2(411, 197), V2(436, 249)]
drawListOfPoints(poligono3)
boundaryFillin(379,248, colorbordeado, colorrelleno)


#Poligono 4 y 5
poligono5 = [ V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170) ]
drawListOfPoints(poligono5)
boundaryFillin(685,173, colorbordeado, colorrelleno)

poligono4 = [ V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52),
V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230),
V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180) ]
drawListOfPoints(poligono4)

rend.glFinish("output.bmp")
# rend.glPoint(537,37, color(colorrelleno[0], colorrelleno[1], colorrelleno[2]))
boundaryFillinALT(422,176, colorbordeado, colorrelleno)



rend.glFinish("output.bmp")
