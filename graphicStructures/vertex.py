import numpy as np
from vector import Vector


class Vertex:

	def __init__(self, x, y, z, n = None):
		self.x = x
		self.y = y
		self.z = z
		self.faces = []

		self.n = n

	def toTuple(self):
		return (self.x, self.y, self.z)

	def setNormal(self, n):
		self.n = n

	def addAssociatedFace(self, face):
		self.faces.append(face)

	def calculateNormalizedAverageNormal(self):

		sumVector = Vector(0,0,0)
		noFaces = 0

		for face in self.faces:
			sumVector = Vector.add(
				sumVector,
				face.getSurfaceNormal()
			)

			noFaces = noFaces + 1

		print(sumVector.toTuple())
		print(noFaces)
		return Vector.scalarDivision(sumVector, noFaces)
