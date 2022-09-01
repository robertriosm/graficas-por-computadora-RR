
from gl import Renderer, V3
from texture import Texture
from shaders import gourad, sandy, shark1, anime

width = 600
height = 450

rend = Renderer(width, height)
rend.glLookAt(V3(3, 1, 0), V3(3, 0.5, 3)) 


# PISO

rend.active_texture = Texture("models/textures/sand_texture.bmp")
rend.active_shader = sandy

rend.glLoadModel("models/base/roca_base.obj",
            translate=V3(2,-0.4,0),
            scale = V3(0.03,0.03,0.03),
            rotate=V3(10,0.03,0.03))

rend.glLoadModel("models/base/roca_base.obj",
            translate=V3(3,-0.2,0),
            scale = V3(0.03,0.03,0.03),
            rotate=V3(-1,0.03,-10))

rend.glLoadModel("models/base/roca_base.obj",
            translate=V3(4,-0.5,0),
            scale = V3(0.03,0.03,0.03),
            rotate = V3(-20,-0.03,0.03))


#ROCAS AMBIENTE

rend.active_texture = Texture("models/textures/rock_texture.bmp")
rend.active_shader = gourad

rend.glLoadModel("models/rocks/ObeliskSet01_A.obj",
                translate=V3(0.5,0,-1.2),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_B.obj",
                translate=V3(1,0,-2.4),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_C.obj",
                translate=V3(2,0,-4.6),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_D.obj",
                translate=V3(2.6,0,-5.7),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_E.obj",
                translate=V3(4.8,0,-3.6),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_F.obj",
                translate=V3(3.5,0,-2.4),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_G.obj",
                translate=V3(4.2,0,-0.1),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/ObeliskSet01_H.obj",
                translate=V3(5,0,-0.2),
                scale = V3(0.1,0.1,0.1))

rend.glLoadModel("models/rocks/large_rock.obj",
                translate=V3(4.6,0,-4.2),
                scale = V3(0.03,0.03,0.03))

# SHARKS!!

rend.active_texture = Texture("models/textures/shark_texture.bmp")

rend.active_shader = shark1
rend.glLoadModel("models/objs/Shark.obj",
                translate=V3(3,0.5,-1),
                scale = V3(0.02,0.02,0.02),
                rotate=V3(20,0,8))

rend.active_shader = gourad
rend.glLoadModel("models/objs/Shark.obj",
                translate=V3(3.6,0.65,-1.3),
                scale = V3(0.025,0.025,0.025),
                rotate=V3(10,0,-8))

rend.active_shader = gourad
rend.glLoadModel("models/objs/Shark.obj",
                translate=V3(2.4,0.4,-1.8),
                scale = V3(0.02,0.02,0.02),
                rotate=V3(-10,0,8))

rend.glFinish(f"escena_proyecto.bmp")

