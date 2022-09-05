
from gl import Renderer, V3
from texture import Texture
from shaders import gourad, lava, golden, fallout_VATS, angry, silver, plastilina

width = 600
height = 450

rend = Renderer(width, height)
rend.glLookAt(V3(3.5, 1, 0), V3(5, 0.5, 3))

rend.active_texture = Texture("models/marmol.bmp")

rend.active_shader = gourad
rend.glLoadModel("models/Stone.obj",
                translate = V3(2, 0, 0),
                scale = V3(0.1,0.1,0.1),)

rend.active_shader = lava
rend.glLoadModel("models/Stone.obj",
                translate = V3(3, 0, 0),
                scale = V3(0.1,0.1,0.1))

rend.active_shader = golden
rend.glLoadModel("models/Stone.obj",
                translate = V3(4, 0, 0),
                scale = V3(0.1,0.1,0.1))

rend.active_shader = fallout_VATS
rend.glLoadModel("models/Stone.obj",
                translate = V3(3, 1.4, 0),
                scale = V3(0.1,0.1,0.1),)

rend.active_shader = angry
rend.glLoadModel("models/Stone.obj",
                translate = V3(2, 1.4, 0),
                scale = V3(0.1,0.1,0.1))

rend.active_shader = silver
rend.glLoadModel("models/Stone.obj",
                translate = V3(4, 1.4, 0),
                scale = V3(0.1,0.1,0.1))

rend.glFinish("shaders.bmp")
