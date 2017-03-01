class Vertex:

	def __init__(self, x, y, z, n = None):
		self.x = x
		self.y = y
		self.z = z
		self.faces = {}
		if n != None:
			self.n = n

	def toTuple(self):
		return (self.x, self.y, self.z)

	def setNormal(self, n):
		self.n = n

	def addAssociatedFace(self, face):
		self.faces.append(face)

	def calculateNormalizedAverageNormal():
		x = 0
		total = 0
		for face in faces:
			total = face.getSurfaceNormal
