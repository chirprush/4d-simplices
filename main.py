from dataclasses import dataclass
from math import sqrt, cos, sin, pi
from typing import List
from sys import stderr

@dataclass
class Vec2:
    x: float
    y: float

@dataclass
class Vec3:
    x: float
    y: float
    z: float

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        return self / self.length()

    def to_vec2(self):
        return Vec2(self.x, self.y)

    def rotateX(self, theta):
        return Vec3(
            self.x,
            self.y * cos(theta) - self.z * sin(theta),
            self.y * sin(theta) + self.z * cos(theta)
        )

    def rotateY(self, theta):
        return Vec3(
            self.x * cos(theta) + self.z * sin(theta),
            self.y,
            -self.x * sin(theta) + self.z * cos(theta)
        )

    def rotateZ(self, theta):
        return Vec3(
            self.x * cos(theta) - self.y * sin(theta),
            self.x * sin(theta) + self.y * cos(theta),
            self.z
        )

    def __add__(self, other):
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, k):
        return Vec3(
            self.x * k,
            self.y * k,
            self.z * k
        )

    def __truediv__(self, k):
        return Vec3(
            self.x / k,
            self.y / k,
            self.z / k
        )

@dataclass
class Vec4:
    x: float
    y: float
    z: float
    w: float

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        return self / self.length()

    def to_vec3(self):
        return Vec3(self.x, self.y, self.z)

    def rotateXY(self, theta):
        return Vec4(
            self.x * cos(theta) + self.y * sin(theta),
            -self.x * sin(theta) + self.y * cos(theta),
            self.z,
            self.w
        )

    def rotateXZ(self, theta):
        return Vec4(
            self.x * cos(theta) - self.z * sin(theta),
            self.y,
            self.x * sin(theta) + self.z * cos(theta),
            self.w
        )

    def rotateXW(self, theta):
        return Vec4(
            self.x * cos(theta) + self.w * sin(theta),
            self.y,
            self.z,
            -self.x * sin(theta) + self.w * cos(theta)
        )

    def rotateYZ(self, theta):
        return Vec4(
            self.x,
            self.y * cos(theta) + self.z * sin(theta),
            -self.y * sin(theta) + self.z * cos(theta),
            self.w
        )

    def rotateYW(self, theta):
        return Vec4(
            self.x,
            self.y * cos(theta) - self.w * sin(theta),
            self.z,
            self.y * sin(theta) + self.w * cos(theta)
        )

    def rotateZW(self, theta):
        return Vec4(
            self.x,
            self.y,
            self.z * cos(theta) - self.w * sin(theta),
            self.z * sin(theta) + self.w * cos(theta)
        )

    def __add__(self, other):
        return Vec4(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )

    def __sub__(self, other):
        return Vec4(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        )

    def __mul__(self, k):
        return Vec4(
            self.x * k,
            self.y * k,
            self.z * k,
            self.w * k
        )

    def __truediv__(self, k):
        return Vec4(
            self.x / k,
            self.y / k,
            self.z / k,
            self.w / k
        )

@dataclass
class Edge:
    start: int
    end: int

@dataclass
class Object3d:
    vertices: List[Vec3]
    edges: List[Edge]

    def rotateX(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateX(theta)
            
        return self

    def rotateY(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateY(theta)
            
        return self

    def rotateZ(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateZ(theta)
            
        return self

@dataclass
class Object4d:
    vertices: List[Vec4]
    edges: List[Edge]

    def rotateXY(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateXY(theta)
            
        return self

    def rotateXZ(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateXZ(theta)
            
        return self

    def rotateXW(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateXW(theta)
            
        return self

    def rotateYZ(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateYZ(theta)
            
        return self

    def rotateYW(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateYW(theta)
            
        return self

    def rotateZW(self, theta):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = vertex.rotateZW(theta)
            
        return self

class Simplex3d(Object3d):
    def __init__(self):
        self.vertices = [
            Vec3(0, 0, 0),
            Vec3(1, 0, 0),
            Vec3(0, 1, 0),
            Vec3(0, 0, 1),
        ]

        for i, v in enumerate(self.vertices):
            self.vertices[i] += Vec3(-1/2, -1/2, -1/2)

        self.edges = [Edge(n, m) for n in range(4) for m in range(n + 1, 4)]

class Simplex4d(Object4d):
    def __init__(self):
        self.vertices = [
            Vec4(0, 0, 0, 0),
            Vec4(1, 0, 0, 0),
            Vec4(0, 1, 0, 0),
            Vec4(0, 0, 1, 0),
            Vec4(0, 0, 0, 1),
        ]

        for i, v in enumerate(self.vertices):
            self.vertices[i] += Vec4(-1/2, -1/2, -1/2, -1/2)

        self.edges = [Edge(n, m) for n in range(5) for m in range(n + 1, 5)]

@dataclass
class Projection:
    vertices: List[Vec2]
    edges: List[Edge]

    def to_tikz(self):
        output = []

        output.append(r"\begin{tikzpicture}[scale=2]")

        for i, vertex in enumerate(self.vertices):
            output.append(r"  \node (v%d) at (%f, %f) {};" % (i, vertex.x, vertex.y))
            output.append(r"  \fill (v%d) circle(0.01);" % i)
        
        for edge in self.edges:
            output.append(r"  \draw (v%d.center) -- (v%d.center);" % (edge.start, edge.end))

        output.append(r"\end{tikzpicture}")

        return '\n'.join(output)

def project3to2(camera, plane_z, shape):
    vertices = []
    edges = shape.edges

    for vertex in shape.vertices:
        direction = (vertex - camera).normalize()
        # t = plane / direction.z
        t = (plane_z - camera.z) / direction.z
        image = direction * t + camera
        print(image, file=stderr)
        vertices.append(image.to_vec2())
    
    return Projection(vertices, edges)

def project4to3(camera, plane_w, shape):
    vertices = []
    edges = shape.edges

    for vertex in shape.vertices:
        # print(vertex - camera, (vertex-camera).length(), (vertex - camera).normalize())
        direction = (vertex - camera).normalize()
        t = (plane_w - camera.w) / direction.w
        image = direction * t + camera
        print(image, file=stderr)
        vertices.append(image.to_vec3())
    
    # return Projection(vertices, edges)
    return Object3d(vertices, edges)

# 3d case
"""
camera = Vec3(0, 0, -2)
plane = -1
simplex = Simplex3d()

projection = project3to2(camera, plane, simplex)
"""

camera4 = Vec4(0, 0, 0, -2)
camera3 = Vec3(0, 0, -2)

plane = -1
simplex = Simplex4d().rotateXW(pi / 4)

obj = project4to3(camera4, plane, simplex)
projection = project3to2(camera3, plane, obj)

if True:
    print(r"""
\documentclass{standalone}
\usepackage{tikz}

\begin{document}
""".lstrip())
    print(projection.to_tikz())

    print("\n\\end{document}")
