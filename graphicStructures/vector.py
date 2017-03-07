import math

class Vector:

    def __init__(self, *args):
        self.components = args

    #Calculate the magnitude of this 3-dimensional vector
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def toTuple(self):
        return tuple((x for x in self.components))

    @staticmethod
    def scalarDivision(vector, scalar):

        components = []

        for x in vector.components:
            components.append(x/float(scalar))

        return Vector(*components)


    @staticmethod
    def generateVector(p1, p2):

        components = []

        for x in range(len(p1.toTuple())):
            components.append(p2.toTuple()[x] - p1.toTuple()[x])

        return Vector(*components)
    @staticmethod
    def add(v1, v2):

        v3 = []

        for x in range(len(v1.components)):
            v3.append(v1.components[x] + v2.components[x])

        return Vector(*v3)
    @staticmethod
    def cross(v1, v2):

        """
        Returns a new vector that is the cross product
        of the 2 supplied vectors. Only works on
        vectors of 3 dimensions.
        """

        #Retreive components
        x1, y1, z1 = v1.toTuple()
        x2, y2, z2 = v2.toTuple()

        #calculate components of new vector
        x3 = (y1 * z2) - (z1 * y2)
        y3 = (z1 * x2) - (x1 * z2)
        z3 = (x1 * y2) - (y1 * x2)

        return Vector(x3, y3, z3)

if __name__ == '__main__':

    from vertex import Vertex

    v1 = Vertex(1,0,0)
    v2 = Vertex(0,1,0)
    v3 = Vertex(0,0,1)

    print(v1.toTuple())
    vect1 = Vector(0, 1, 0)
    vect2 = Vector(0, 0, 1)
    x, y, z = vect1.toTuple()
    print(vect1.toTuple())
    print(x)
    print(vect1.magnitude())
    print(Vector.add(vect1, vect2).toTuple())
    print(Vector.scalarDivision(vect1, 2).toTuple())
    print(Vector.cross(vect1, vect2).toTuple())
