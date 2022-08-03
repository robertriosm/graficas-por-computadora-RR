"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
LIBRERIA 3D DE GRAFICAS DE BITMAPS
"""

import struct
from math import sin, log
from collections import namedtuple
from object3d import Object3D

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

def char(c: str):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w: int):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d: int):
    # 4 byte
    return struct.pack('=l', d)


def color(r: float, g: float, b: float):
    return bytes([int(b * 255), 
                  int(g * 255), 
                  int(r * 255)])


def glCreateWindow(width: int, height: int):
    return MyRenderer(width, height)


class MyRenderer(object):

    # ------------------------------- constructor, glInit ------------------------------- 

    def __init__(self, width: int, height: int):
        # resolution
        self.width = width
        self.height = height
        # bg color
        self.clearColor = color(0, 0, 0)
        self.currcolor = color(1, 1, 1)
        # viewport
        self.glViewPort(0, 0, self.width, self.height)
        # fill the image
        self.glClear()

    # ------------------------------- viewport controls ------------------------------- 

    def glViewPort(self, x: int, y: int, width: int, height: int):
        self.vpx = int(x)
        self.vpy = int(y)
        self.vpwidth = int(width)
        self.vpheight = int(height)


    def glClearViewport(self, clr = None):
        for x in range(self.vpx, self.vpx + self.vpwidth):
            for y in range(self.vpy, self.vpy + self.vpheight):
                self.glPoint(x, y, clr)


    # ------------------------------- points drawing ------------------------------- 

    # point with window coordinates
    def glPoint(self, x: int, y: int, pcolor:bytes = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = pcolor or self.currcolor


    # viewport coordinates, normalized device coordinates
    def glNDCPoint(self, ndcx: int, ndcy: int, clr = None):
        x = (ndcx + 1) * (self.vpwidth / 2) + self.vpx
        y = (ndcy + 1) * (self.vpheight / 2) + self.vpy
        
        x = int(x)
        y = int(y)

        self.glPoint(x, y, clr)

    # draw experimental sin
    def glVertex(self):
        for x in range(self.vpx, self.vpx + self.vpwidth):
            self.glPoint(x, int(sin(x)*2) + self.vpy*2, self.currcolor)
        for x in range(self.vpx, self.vpx + self.vpwidth):
            self.glPoint(x, int(log(x, 2)*2) + self.vpy*4, self.currcolor)

    # ------------------------------- clear ------------------------------- 

    def glClear(self):
        self.pixels = [[ self.clearColor for y in range(self.height) ] 
                       for x in range(self.width) ]


    def glClearColor(self, r: float, g: float, b: float):
        self.clearColor = color(r, g, b)
    
    # ------------------------------- color controls ------------------------------- 
    
    def glColor(self, r: float, g: float, b: float):
        self.currcolor = color(r, g, b)

    # ------------------------------- write file ----------------------------

    def glFinish(self, filename: str):
        with open(filename, 'wb') as file:
            # file Header
            # 2 bytes
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            # 4 bytes, image size
            file.write(dword(14 + 40 + (self.height * self.width * 3)))
            # 2 bytes, reserved
            file.write(dword(0))
            # 2 bytes
            # 4 bytes
            file.write(dword(14 + 40))

            # info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0)) 
            # image size
            file.write(dword(self.width * self.height * 3))
            # reserved
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # fill image
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])


    # ------------------------------- draw line with Bresenham algorithm ----------------------------
    def glLine(self, v0, v1, clr = None):
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        # Si p0 == p1, dibujar solo un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0,clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        step = dy > dx
        
        if step:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si Xo > Xf, intercambiar los puntos para dibujar de izquierda -> derecha       
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if step:
                # en y 
                self.glPoint(y, x, clr)
            else:
                # en x
                self.glPoint(x, y, clr)
            offset += m
            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
                limit += 1

    # ------------------------------- fill polygons (triangles) ----------------------------

    def glTriangle_std(self, A, B, C, clr = None):
        
        # change/share vertices
        if A.y < B.y:
            A, B = B, A

        if A.y < C.y:
            A, C = C, A

        if B.y < C.y:
            B, C = C, B

        self.glLine(A,B, clr)
        self.glLine(B,C, clr)
        self.glLine(C,A, clr)

        def flatBottom(vA,vB,vC):
            try:
                mBA = (vB.x - vA.x) / (vB.y - vA.y)
                mCA = (vC.x - vA.x) / (vC.y - vA.y)
            except:
                pass
            else:
                x0 = vB.x
                x1 = vC.x
                for y in range(int(vB.y), int(vA.y)):
                    self.glLine(V2(x0, y), V2(x1, y), clr)
                    x0 += mBA
                    x1 += mCA

        def flatTop(vA,vB,vC):
            try:
                mCA = (vC.x - vA.x) / (vC.y - vA.y)
                mCB = (vC.x - vB.x) / (vC.y - vB.y)
            except:
                pass
            else:
                x0 = vA.x
                x1 = vB.x
                for y in range(int(vA.y), int(vC.y), -1):
                    self.glLine(V2(x0, y), V2(x1, y), clr)
                    x0 -= mCA
                    x1 -= mCB

        # upper face
        if B.y == C.y:
            flatBottom(A,B,C)
        # lower face
        elif A.y == B.y:
            flatTop(A,B,C)
        # find intercept
        else:
            D = V2( A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x), B.y)
            flatBottom(A,B,D)
            flatTop(B,D,C)
    
    # bc triangle
    def glTriangle_bc():
        pass

    # ------------------------------- load .obj models ----------------------------
    def load_object(self, filename: str, translate: tuple, scale: tuple):
        model = Object3D(filename)
    
        for face in model.faces:
            vcount = len(face)
            for j in range(vcount):
                f1 = face[j][0]
                f2 = face[(j + 1) % vcount][0]

                v1 = model.vertices[int(f1) - 1]
                v2 = model.vertices[int(f2) - 1]
        
                x1 = round((v1[0] + translate[0]) * scale[0])
                y1 = round((v1[1] + translate[1]) * scale[1])
                x2 = round((v2[0] + translate[0]) * scale[0])
                y2 = round((v2[1] + translate[1]) * scale[1])

                self.glLine(V2(x1, y1), V2(x2, y2))


def drawPolygon(polygon: list, render: MyRenderer, clr: bytes = None):
    for i in range(len(polygon)):
        render.glLine(polygon[i], polygon[ (i + 1) % len(polygon)], clr)

def fragmentShader(render: MyRenderer, **kwargs):
    return 1,0,1