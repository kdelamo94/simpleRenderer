class Face:

	def __init__(self, v1, v2, v3):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3

	def toVertexTuple(self):
		return (self.v1, self.v2, self.v3)

	#def setVertexNormals():
