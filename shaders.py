"""
SHADERS
"""

import rrmath as ml
from texture import Texture
import random


def gourad(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def lava(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    plasti = (0.2,0.1,0.8)

    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tU, tV)
        b *= plasti[0]
        g *= texColor[1]
        r *= plasti[2]

    return r, g, b


def anime(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def fallout_VATS(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    green = (0,1,0)

    b += green[2] * glowAmount
    g += green[1] * glowAmount
    r += green[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def silver(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255
    greyscale = [0.5, 0.5, 0.5]
    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity 
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    brightness = (1,1,1)

    b += brightness[2] * glowAmount
    g += brightness[1] * glowAmount
    r += brightness[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def angry(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255
    greyscale = [0.5, 0.5, 0.5]
    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity 
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    anger = (0.5,0,0)

    b += anger[2] * glowAmount
    g += anger[1] * glowAmount
    r += anger[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def shark1(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255
    ton = [0.2, 0.3, 0.1]
    if render.active_texture:
        
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal =  ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity 
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    anger = (0,0,0.2)

    b += anger[2]
    g += anger[1]
    r += anger[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def shark2(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255
    ton = [0.2, 0.3, 0.1]
    if render.active_texture:
        
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal =  ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity 
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    anger = (0,0,0.2)

    b += anger[2]
    g += anger[1]
    r += anger[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def shark3(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255
    ton = [0.2, 0.3, 0.1]
    if render.active_texture:
        
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal =  ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity 
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    camForward = (render.camMatrix[0][2],
                  render.camMatrix[1][2],
                  render.camMatrix[2][2])

    glowAmount = 1 - ml.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    anger = (0,0,0.2)

    b += anger[2]
    g += anger[1]
    r += anger[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def sandy(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2] 
        g *= texColor[1] 
        r *= texColor[0] 
        
    triangleNormal =  ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = render.dirLight
    intensity = ml.dot(triangleNormal, [-dirLight.x,-dirLight.y,-dirLight.z])

    r *= intensity
    b *= intensity 
    g *= intensity

    avgrgb = (r + g + b) / 3

    r = avgrgb
    b = avgrgb
    g = avgrgb

    yellowish = (0.91,0.85,0.28)

    b += yellowish[2] / 5
    g += yellowish[1] / 5
    r += yellowish[0] / 5

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0