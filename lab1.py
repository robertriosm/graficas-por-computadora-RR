# controlador para ejecutar el lab 1

from gl import Renderer, color, V2
from sys import setrecursionlimit

setrecursionlimit(5000)
rend = Renderer(1000, 1000)
rend.glColor(1,1,1)
border_color = color(1,1,1)
fill_color = color(0.9,0.9,0.9)

def draw_polygon(points: list):
    for i in range(len(points)):
        if i == len(points)-1:
            rend.glLine(points[0], points[i])
            break
        rend.glLine(points[i], points[i+1])
        
def recursive_lines(x, y):
    pixel_color = rend.getPixel(x, y)
    if pixel_color != border_color and pixel_color != fill_color:
        rend.glPoint(x, y, fill_color)
        recursive_lines(x + 1, y)
        recursive_lines(x - 1, y)
        recursive_lines(x, y + 1)
        recursive_lines(x, y - 1)

pol1 = [V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345), 
        V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385),
        V2(205, 410), V2(193, 383)]
pol2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]
pol3 = [V2(377, 249), V2(411, 197), V2(436, 249)]
pol4 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]
pol5 = [V2(413, 177), V2(448, 159), V2(502, 88),  V2(553, 53), 
        V2(535, 36),  V2(676, 37),  V2(660, 52),  V2(750, 145), 
        V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), 
        V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214), 
        V2(517, 144), V2(466, 180)]

subpol1 = [pol5[0],pol5[1],pol5[-1]]
subpol2 = [pol5[1],pol5[2],pol5[-2],pol5[-1]]
subpol3 = [pol5[2],pol5[3],pol5[-2]]
subpol4 = [pol5[3],pol5[4],pol5[5],pol5[6]]
subpol5 = [pol5[6],pol5[7],pol5[8],pol5[9]]
subpol6 = [pol5[3],pol5[6],pol5[9],pol5[-2]]
subpol7 = [pol5[9],pol5[10],pol5[15],pol5[-2]]
subpol8 = [pol5[11],pol5[12],pol5[13],pol5[14]]

draw_polygon(pol1)
recursive_lines(180, 380)

draw_polygon(pol2)
recursive_lines(321, 334)

draw_polygon(pol3)
recursive_lines(379,248)

draw_polygon(subpol1)
recursive_lines(448,177)

draw_polygon(subpol2)
recursive_lines(467, 159)

draw_polygon(subpol3)
recursive_lines(518, 88)

draw_polygon(subpol4)
recursive_lines(553, 52)

draw_polygon(subpol5)
#recursive_lines(760, 180)

draw_polygon(subpol6)
# recursive_lines(414, 177)

draw_polygon(subpol7)
# recursive_lines(414, 177)

draw_polygon(subpol8)
#recursive_lines(582, 229)

draw_polygon(pol4)

rend.glFinish("lab_1.bmp")