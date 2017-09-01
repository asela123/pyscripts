#-------------------------------------------------------------------------------
# Name:        3d
# Purpose:
#
# Author:      ?????_?????
#
# Created:     30/08/2017
# Copyright:   (c) ?????_????? 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import random
import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )


edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        for babushka in (1,2,3,4,5):
            for vertex in edge:
                big_vertex = map(lambda x: x * babushka, vertices[vertex])
                glVertex3fv(big_vertex)
            for vertex in edge:
                big_vertex = map(lambda x: x * babushka, vertices[vertex])
                glVertex3fv(big_vertex)
                glVertex3fv(vertices[vertex])
    glEnd()



def rand_pol():
    fig = plt.figure()
    ax = Axes3D(fig)
    # x = [0,1,1,0]
    # y = [0,0,1,1]
    # z = [0,1,0,1]
    # verts = [zip(x, y,z)]
    # ax.add_collection3d(Poly3DCollection(verts))
    # plt.show()
    for i in range(10):
        x = rand3()
        y = rand3()
        z = rand3()
        vtx = [x,y,z]
        tri = a3.art3d.Poly3DCollection([vtx])
        tri.set_color(colors.rgb2hex(rand3()))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
    plt.show()
    pass


def rand3():
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        return [x,y,z]



if __name__ == '__main__':
    # rand_pol()
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glScalef(0.2,0.2,0.2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
