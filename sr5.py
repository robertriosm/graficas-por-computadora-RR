
from gl import Renderer, V3
from texture import Texture
from shaders import gourad

width = 960
height = 540

rend = Renderer(width, height)

rend.active_texture = Texture("models/paper.bmp")
rend.active_shader = gourad

opcion = ""
count = 0
opciones = ["1", "2", "3", "4"]

while opcion != "5":
    rend.glClear()
    # fovxd=int(input("fov: "))
    #rend.glProjectionMatrix() #fov=fovxd)
    #rend.glViewMatrix()
    # print("Hola, escoge un angulo:"
    #     "\n1) medium angle shot"
    #     "\n2) high angle shot"
    #     "\n3) low angle shot"
    #     "\n4) dutch angle shot"
    #     "\n5) salir del programa"
    # )
    # opcion = input("Tu opcion: ")

    # if opcion == "1":
    #     shot_angle = medium_shot_angle

    # elif opcion == "2":
    #     shot_angle = high_shot_angle
    #     rend.glProjectionMatrix(fov=80)

    # elif opcion == "3":
    #     shot_angle = low_shot_angle
    #     rend.glProjectionMatrix(fov=70)

    # elif opcion == "4":
    #     shot_angle = dutch_shot_angle
    #     rend.glProjectionMatrix(fov=50)

    # elif opcion == "5":
    #     print("adios")

    # else:
    #     pass
    
    # if opcion in opciones:
    #     x = int(input("ingresa x: "))
    #     y = int(input("ingresa y: "))
    #     z = int(input("ingresa z: "))
        
    #     rend.glLookAt(V3(0,0,0), V3(x,y,z))
    #     rend.glLoadModel("models/Stone.obj",
    #             scale = V3(0.1,0.1,0.1))
    #     rend.glFinish(f"photo_{count}.bmp")
    #     count += 1
    
    #     print("revisa el directorio para ver la foto.")

    x = int(input("rotacion x: "))
    y = int(input("rotacion y: "))
    z = int(input("rotacion z: "))
    
    rend.glLookAt(V3(0,0,0), V3(x,y,z))
    rend.glLoadModel("models/Stone.obj",
            scale = V3(0.1,0.1,0.1))
    rend.glFinish(f"photo_{count}.bmp")
    count += 1
    opcion = input("5? ")

# high: 0,2,1 
# low: 0,-1,1 ; fov=40