import numpy as np
from vector import Vector
class Face:

	def __init__(self, v1, v2, v3):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3

		vect1 = Vector.generateVector(v1, v2)
		vect2 = Vector.generateVector(v1, v3)
		self.n = Vector.cross(vect1, vect2)

		v1.addAssociatedFace(self)
		v2.addAssociatedFace(self)
		v3.addAssociatedFace(self)

	def toVertexTuple(self):
		return (self.v1, self.v2, self.v3)

	def getSurfaceNormal(self):
		return self.n

if __name__ == '__main__':
	from vertex import Vertex

	v1 = Vertex(0,0,0)
	v2 = Vertex(0,1,0)
	v3 = Vertex(0,0,1)

	face = Face(v1, v2, v3)

	print(face.getSurfaceNormal().toTuple())
