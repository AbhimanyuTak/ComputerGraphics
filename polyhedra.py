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


vertex = 5.0
a = 3.5
global temp
temp = 0


def init():
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glShadeModel(GL_FLAT)
  glEnable(GL_DEPTH_TEST)


def display():
   #global temp
   glClear( GL_COLOR_BUFFER_BIT)
   #gluLookAt(0.0, 0.0, 16, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
   
   #sees the value on key press
   if temp == 1:
     cuboid()
   elif temp == 2:
     clip_edges()
   
   #glutSwapBuffers()

# A simple cuboid is implementd
def cuboid():
   glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
   #gluLookAt(0.0, 0.0, 16, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

   glBegin(GL_LINE_LOOP)
   #glColor4f( 0.0, 1.0, 1.0, 0.0 )     
   glVertex3f(  vertex, -vertex, -vertex )    
   glVertex3f(  vertex,  vertex, -vertex )   
   glVertex3f( -vertex,  vertex, -vertex )        
   glVertex3f( -vertex, -vertex, -vertex )   
   glEnd()

   #White side - BACK
   glBegin(GL_LINE_LOOP)
   #glColor3f(   1.0,  1.0, 0.0 )
   glVertex3f(  vertex, -vertex, vertex )
   glVertex3f(  vertex,  vertex, vertex )
   glVertex3f( -vertex,  vertex, vertex )
   glVertex3f( -vertex, -vertex, vertex )
   glEnd()
 
   #Purple side - RIGHT
   glBegin(GL_LINE_LOOP)
   #glColor3f(  1.0,  0.0,  1.0 )
   glVertex3f( vertex, -vertex, -vertex )
   glVertex3f( vertex,  vertex, -vertex )
   glVertex3f( vertex,  vertex,  vertex )
   glVertex3f( vertex, -vertex,  vertex )
   glEnd()
 
   #Green side - LEFT
   glBegin(GL_LINE_LOOP)
   #glColor3f(   0.0,  1.0,  0.0 )
   glVertex3f( -vertex, -vertex,  vertex )
   glVertex3f( -vertex,  vertex,  vertex )
   glVertex3f( -vertex,  vertex, -vertex )
   glVertex3f( -vertex, -vertex, -vertex )
   glEnd()
 
   #Blue side - TOP
   glBegin(GL_LINE_LOOP)
   #glColor3f(   0.0,  0.0,  1.0 )
   glVertex3f(  vertex,  vertex,  vertex )
   glVertex3f(  vertex,  vertex, -vertex )
   glVertex3f( -vertex,  vertex, -vertex )
   glVertex3f( -vertex,  vertex,  vertex )
   glEnd()
 
   #Red side - BOTTOM
   glBegin(GL_LINE_LOOP)
   #glColor3f(   1.0,  0.0,  0.0 )
   glVertex3f(  vertex, -vertex, -vertex )
   glVertex3f(  vertex, -vertex,  vertex )
   glVertex3f( -vertex, -vertex,  vertex )
   glVertex3f( -vertex, -vertex, -vertex )
   glEnd()

   glFlush()



def reshape(w,h):
   glViewport(0, 0, w, h)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glFrustum(-10.0, 10.0, -10.0, 10.0, 10.0, 25.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt(0.0, 0.0, 16, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
 

def mykey(key, x, y):
   global temp

   if key=='s': # Camera
     temp = 1
   elif key=='d':
     temp = 2
   elif key=='q':
     sys.exit()
   
   glutPostRedisplay()


# A cuboid with clipped edgec
def clip_edges():
   glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

   glBegin(GL_LINE_LOOP)
   #glColor3f( 1.0, 1.0, 1.0 )     
   glVertex3f(  vertex - a, -vertex,     -vertex ) 
   glVertex3f(  vertex,     -vertex + a, -vertex )
   glVertex3f(  vertex,      vertex - a, -vertex )
   glVertex3f(  vertex - a,  vertex,     -vertex )    
   glVertex3f( -vertex + a,  vertex,     -vertex ) 
   glVertex3f( -vertex,      vertex - a, -vertex )
   glVertex3f( -vertex,     -vertex + a, -vertex )
   glVertex3f( -vertex + a, -vertex,     -vertex )        
   glEnd()

   glBegin(GL_LINE_LOOP)
   #glColor3f( 1.0, 1.0, 1.0 )     
   glVertex3f(  vertex - a, -vertex,     vertex ) 
   glVertex3f(  vertex,     -vertex + a, vertex )
   glVertex3f(  vertex,      vertex - a, vertex )
   glVertex3f(  vertex - a,  vertex,     vertex )    
   glVertex3f( -vertex + a,  vertex,     vertex ) 
   glVertex3f( -vertex,      vertex - a, vertex )
   glVertex3f( -vertex,     -vertex + a, vertex )
   glVertex3f( -vertex + a, -vertex,     vertex )        
   glEnd()

   glBegin(GL_LINE_LOOP)
   #glColor3f(  1.0,  0.0,  1.0 )
   glVertex3f( vertex,  vertex - a, -vertex 	)
   glVertex3f( vertex,  vertex,     -vertex + a )
   glVertex3f( vertex,  vertex,      vertex - a )
   glVertex3f( vertex,  vertex - a,  vertex 	)
   glVertex3f( vertex, -vertex + a,  vertex 	)
   glVertex3f( vertex, -vertex,      vertex - a )
   glVertex3f( vertex, -vertex,     -vertex + a )
   glVertex3f( vertex, -vertex + a, -vertex     )
   glEnd()

   glBegin(GL_LINE_LOOP)
   #glColor3f(  1.0,  0.0,  1.0 )
   glVertex3f( -vertex,  vertex - a, -vertex 	)
   glVertex3f( -vertex,  vertex,     -vertex + a )
   glVertex3f( -vertex,  vertex,      vertex - a )
   glVertex3f( -vertex,  vertex - a,  vertex 	)
   glVertex3f( -vertex, -vertex + a,  vertex 	)
   glVertex3f( -vertex, -vertex,      vertex - a )
   glVertex3f( -vertex, -vertex,     -vertex + a )
   glVertex3f( -vertex, -vertex + a, -vertex     )
   glEnd()

   glBegin(GL_LINE_LOOP)
   #glColor3f(   0.0,  0.0,  1.0 )
   glVertex3f(  vertex - a,  vertex, -vertex     )
   glVertex3f(  vertex,      vertex, -vertex + a )
   glVertex3f(  vertex,      vertex,  vertex - a )
   glVertex3f(  vertex - a,  vertex,  vertex     )
   glVertex3f( -vertex + a,  vertex,  vertex     )
   glVertex3f( -vertex,      vertex,  vertex - a )
   glVertex3f( -vertex,      vertex, -vertex + a )
   glVertex3f( -vertex + a,  vertex, -vertex     )
   glEnd()

   glBegin(GL_LINE_LOOP)
   #glColor3f(   0.0,  0.0,  1.0 )
   glVertex3f(  vertex - a,  -vertex, -vertex     )
   glVertex3f(  vertex,      -vertex, -vertex + a )
   glVertex3f(  vertex,      -vertex,  vertex - a )
   glVertex3f(  vertex - a,  -vertex,  vertex     )
   glVertex3f( -vertex + a,  -vertex,  vertex     )
   glVertex3f( -vertex,      -vertex,  vertex - a )
   glVertex3f( -vertex,      -vertex, -vertex + a )
   glVertex3f( -vertex + a,  -vertex, -vertex     )
   glEnd()
   
 
   glFlush()
 



glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
##glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('Polyhedra')
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(mykey)
glutMainLoop()