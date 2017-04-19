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

glMaterialColor = (1.0, 0.0, 0.0, 1.0)
glLightColor = (1.0, 1.0, 1.0, 1.0)

def generateVertexNormals(model):
    for face in model.faces:
        for vertex in face.toVertexTuple():
            vertex.n = vertex.calculateNormalizedAverageNormal()

def renderFrame(model):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    for face in model.faces:
        vertices = face.toVertexTuple()
        for idx, vertex in enumerate(vertices):

            glVertex3fv(vertex.toTuple())
            glVertex3fv(vertices[(idx + 1)%len(vertices)].toTuple())
    glEnd()
def renderBasic(model):

    glBegin(GL_TRIANGLES)

    for face in model.faces:
        for vertex in face.toVertexTuple():
            glNormal3fv(vertex.n.toTuple())
            glVertex3fv(vertex.toTuple())

    glEnd()

def initMaterial():
    glClearColor(0, 0, 0, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, glMaterialColor)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, glMaterialColor)
    #glMaterialfv(GL_FRONT, GL_SHININESS, (80.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, glMaterialColor)

def initLighting():

    glShadeModel(GL_SMOOTH)
    glLightfv(GL_LIGHT0, GL_POSITION, (2, 2, -2, 0))

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)

#process a model file for rendering (order the triangles by shared edges)
def main():
    filename = sys.argv[1]
    MyModel = load(filename)
    generateVertexNormals(MyModel)
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.0, 50.0)
    glTranslatef(-.2, -.2, -5)

    initMaterial()
    initLighting()

    iteration = 0
    prevtime = time.clock()

    translateOn = False
    rotateOn = False

    while True:
        iteration+=1
        #print((prevtime - time.clock()))
        prevtime = time.clock()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print(glGetString(GL_VERSION))
                pygame.quit()
                quit()


            if event.type == pygame.MOUSEMOTION:

                #Use Mouse to rotate object
                if rotateOn:
                    glRotatef(1, event.rel[1], event.rel[0], 0)

                #Use Mouse to translate object
                if translateOn:
                    glTranslatef(event.rel[0]/100.0, 0 - event.rel[1]/100.0, 0)

            if event.type == pygame.MOUSEBUTTONUP:

                #Left Click Release
                if event.button == 1:
                    translateOn = False

                #Right Click Release
                if event.button == 3:
                    rotateOn = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                #Left Click
                if event.button == 1:
                    translateOn = True
                    rotateOn = False

                #Right Click
                if event.button == 3:
                    rotateOn = True
                    translateOn = False

                #Zoom Out
                if event.button == 4:
                    glTranslatef(0, 0, -.3)

                #Zoom In
                if event.button == 5:
                    glTranslatef(0, 0, .3)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        renderBasic(MyModel)
        #renderFrame(MyModel)
        pygame.display.flip()

main()
