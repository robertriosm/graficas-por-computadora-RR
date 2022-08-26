
# controlador para ejecutar el sr5

from gl import Renderer, V3
from texture import Texture
from shaders import gourad

width = 960
height = 540

rend = Renderer(width, height)

rend.active_texture = Texture("models/Stone.bmp")
rend.active_shader = gourad

high_angle = V3(0,2,1)
low_angle = V3(0,-1,1)
medium_angle = V3(0,0,1)
dutch_angle = V3(0,0,1)

opcion = ""
count = 0
opciones = ["1", "2", "3", "4"]

while opcion != "5":
    rend.glClear()
    rotation = V3(0,0,0)
    translation = V3(0,0,0)
    print("Hola, escoge un angulo:"
        "\n1) medium angle shot"
        "\n2) high angle shot"
        "\n3) low angle shot"
        "\n4) dutch angle shot"
        "\n5) salir del programa"
    )
    opcion = input("Tu opcion: ")

    if opcion == "1":
        angle = medium_angle
        rend.glProjectionMatrix(fov=40)
        translation = V3(0,-0.5,-2)

    elif opcion == "2":
        angle = high_angle
        rend.glProjectionMatrix()

    elif opcion == "3":
        angle = low_angle
        rend.glProjectionMatrix(fov=40)

    elif opcion == "4":
        angle = dutch_angle
        rend.glProjectionMatrix(fov=40)
        rotation = V3(10,0,25)
        translation = V3(0,-0.5,-2)

    elif opcion == "5":
        print("adios")

    else:
        pass
    
    if opcion in opciones:
        rend.glLookAt(V3(0,0,0), angle)
        rend.glLoadModel("models/Earth 2K.obj",
                scale = V3(0.1,0.1,0.1),
                translate = translation,
                rotate = rotation)
        rend.glFinish(f"photoshot!/photo_{count}.bmp")
        count += 1
        print("Revisa el directorio 'photoshot!' para ver la foto.")
    
