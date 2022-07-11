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

def color(r: int, g: int, b: int):
    return bytes([int(b * 255), 
                  int(g * 255), 
                  int(r * 255),])

def encode_bytes(p: str):
    return bytes(p.encode('ascii'))

class MyRenderer(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.clearColor = color(0, 0, 0)

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        pass

    def glViewPort(self, x, y, width, height):
        pass

    def glClear(self):
        self.pixels = []

    def glClearColor(self, r, g, b):
        pass

    def glPoint(self, x, y):
        pass

    def glColor(self, r, g, b):
        pass

    def glFinish(self, filename: str):
        with open(filename, 'wb') as file:
            # file Header
            # 2 bytes
            file.write(encode_bytes('B'))
            file.write(encode_bytes('M'))
            # 4 bytes, image size
            file.write(dword(54 + (self.height * self.width * 3)))
            # 2 bytes, reserved
            file.write(dword(0))
            # 2 bytes
            # 4 bytes
            file.write(dword(54))

            # info Header
            file.write(dword(0))
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
