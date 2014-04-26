#!/usr/bin/python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

#  planet.py

from sys import exit
from math import *

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except: print '''ERROR: PyOpenGL not installed properly.'''

rotation = 0.0
radius = 20

#implemented a primitve
def circle():
    glColor3d(0.8, 0.6, 0.8)
    glBegin(GL_POLYGON)
    for ang in range(0, 360, 3):
        #glColor3d(0.8, 0.6, 0.8)
        #glColor3f(1-ang/360, 1-ang/360, 1-ang/360)
        glVertex2d(radius*cos(ang*pi/180), radius*sin(ang*pi/180))
    glEnd()
    glFlush()

def init():
    #mat_specular = [1.0, 1.0, 1.0, 1.0]
    #mat_shininess = [50.0]
    light_position = [1.0, 1.0, 1.0, 0.0]
    white_light = [1.0, 1.0, 1.0, 1.0]
    lmodel_ambient = [0.1, 0.1, 0.1, 1.0]

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    #glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    #glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    #glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
    #glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
##    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

def reshape(w, h):
   global r_x, r_z
   glViewport(0, 0, w, h)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-50.0, 50.0, -50.0, 50.0, -25.0, 25.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt(-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def display():
    global rotation
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    
    #Make continuous discs within a circular area
    glPushMatrix()
    for i in xrange(0,360,1):
       glRotatef(i, 0.0, 1.0, 0.0)
       circle()
    for i in xrange(0,360,1):
       glRotatef(i, 1.0, 0.0, 0.0)
       circle()
    glPopMatrix()
    glutSwapBuffers()



glutInit(sys.argv)
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('Sphere')
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
