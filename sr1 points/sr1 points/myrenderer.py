"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
INGENIERIA EN CIENCIAS DE LA COMPUTACION
GRAFICAS POR COMPUTADORA
ROBERTO RIOS, 20979
"""

import struct

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

class MyRenderer(object):

    # constructor
    def __init__(self, height, width):
        # resolution
        self.height = height
        self.width = width
        # bg color  
        self.clearColor = color(0, 0, 0)
        self.currcolor = color(1, 1, 1)
        # fill the image
        self.glClear() 


    def glInit(self):
        pass


    def glCreateWindow(self, width, height):
        pass


    def glViewPort(self, x, y, width, height):
        pass


    def glClear(self):
        self.pixels = [[ self.clearColor for y in range(self.height) ] 
                       for x in range(self.width) ]


    def glClearColor(self, r: float, g: float, b: float):
        self.clearColor = color(r, g, b)


    def glPoint(self, x: int, y: int, pcolor = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = pcolor or self.currcolor


    def glColor(self, r: float, g: float, b: float):
        self.currcolor = color(r, g, b)


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

            # color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
