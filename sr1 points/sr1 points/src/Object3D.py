
class Object3D(object):

    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:

            try:
                prefix, value = line.split(' ', 1)
            except:
                continue
            try:
                #if line:
                    if prefix == 'v': # Vertices
                        self.vertices.append(list(map(float, value.split(' '))))

                    elif prefix == 'vt': # Vertices tex
                        self.texcoords.append(list(map(float, value.split(' '))))

                    elif prefix == 'vn': # Vertices normales
                        self.normals.append(list(map(float, value.split(' '))))

                    elif prefix == 'f': # Faces
                        self.faces.append([list(map(int , face.split('/'))) for face in value.split(' ')])
            except Exception as e:
                print(line)
                print(self.lines.index(line))
                print(e)