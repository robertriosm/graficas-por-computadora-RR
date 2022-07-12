
from myrenderer import MyRenderer

render = MyRenderer(1024, 1024)

render.glClearColor(1, 1, 1)
render.glColor(0, 0, 0)

render.glClear()

render.glPoint(100, 100)


render.glFinish('image.bmp')