import sys

from graphicStructures.model import Model
from graphicStructures.face import Face
from graphicStructures.vertex import Vertex

def load(filename):

	print(filename)

	obj_file = open(filename, 'r')

	# Get all vertices
	vertices = []
	for line in obj_file:
		if line[0] == 'f':
			break

		v_info = line.split()
		v = Vertex(
			float(v_info[1]),
			float(v_info[2]),
			float(v_info[3])
			)
		vertices.append(v)

	#get all faces
	faces = []
	f_info = line.split()
	f = Face(
			vertices[int(f_info[1]) - 1],
			vertices[int(f_info[2]) - 1],
			vertices[int(f_info[3]) - 1]
		)
	faces.append(f)
	print(f_info)
	for line in obj_file:
		f_info = line.split()
		print(f_info)
		f = Face(
			vertices[int(f_info[1]) - 1],
			vertices[int(f_info[2]) - 1],
			vertices[int(f_info[3]) - 1]
		)
		faces.append(f)

	obj_file.close()

	print(len(faces))
	model = Model(faces)

	return model
