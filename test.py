import sys
import time

from objloader.objLoader import load

from graphicStructures.vertex import Vertex
from graphicStructures.face import Face
from graphicStructures.model import Model

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#just a random color set
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

glMaterialColor = (1.0, 0.0, 0.0, 1.0)
glLightColor = (1.0, 1.0, 1.0, 1.0)

def renderBasic(model):
    glBegin(GL_TRIANGLES)

    for face in model.faces:
        x = 0
        for vertex in face.toVertexTuple():
            x+=1
            glColor3fv(colors[0])
            glVertex3fv(vertex.toTuple())

    glEnd()

def renderLighting(model):
    #Set Vertex Materials
    glMaterialfv(GL_FRONT, GL_AMBIENT, glMaterialColor)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, glMaterialColor)
    glMaterialfv(GL_FRONT, GL_SPECULAR, glMaterialColor)

    glEnable(GL_LIGHTING)
    #Set Global Lighting
    glLightfv(GL_LIGHT0, GL_AMBIENT, glLightColor)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, glLightColor)
    glLightfv(GL_LIGHT0, GL_SPECULAR, glLightColor)
    glLightfv(GL_LIGHT0, GL_POSITION, glLightColor)

    renderBasic(model)

#process a model file for rendering (order the triangles by shared edges)
def main():
    filename = sys.argv[1]
    MyModel = load(filename)
    print(MyModel.faces[0].toVertexTuple()[0].toTuple())
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.0, 50.0)
    glTranslatef(-.2, -.2, -5)

    iteration = 0
    prevtime = time.clock()
    while True:
        iteration+=1
        print((prevtime - time.clock()))
        prevtime = time.clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, .5)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        renderBasic(MyModel)
        pygame.display.flip()

main()
