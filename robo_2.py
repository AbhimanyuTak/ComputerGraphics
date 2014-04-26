#!/usr/bin/python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

#  Robot.py

from sys import exit
from math import *

global shoulder, elbow
shoulder = 0.0
elbow = 0.0

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except: print '''ERROR: PyOpenGL not installed properly.'''


r_z = 3.5
flag = 1

TORSO_ANGLE = 40.0
TORSO_RADIUS=0.1
TORSO_HEIGHT=0.4

LUA_ANGLE=180.0
RUA_ANGLE=180.0
UPPER_ARM_HEIGHT=0.2
UPPER_ARM_WIDTH=0.06

LLA_ANGLE=0.0
RLA_ANGLE=0.0
LOWER_ARM_HEIGHT=0.2
LOWER_ARM_WIDTH=0.05

LUL_ANGLE=180.0
RUL_ANGLE=180.0
UPPER_LEG_HEIGHT=0.2
UPPER_LEG_WIDTH=0.07

LLL_ANGLE=0.0
RLL_ANGLE=0.0
LOWER_LEG_HEIGHT=0.2
LOWER_LEG_WIDTH=0.06


SHOLDER_WIDTH = 0.2
HIP_WIDTH = 0.2

HEAD_ANGLE=0.0
HEADX=0.1
HEADY=TORSO_HEIGHT - 0.05

LUAX=-1.0 * SHOLDER_WIDTH / 2
RUAX=SHOLDER_WIDTH / 2
LUAY=RUAY=TORSO_HEIGHT
LLAY=RLAY=LOWER_ARM_HEIGHT

LULX=-1.0 * HIP_WIDTH / 2
RULX=HIP_WIDTH / 2
LULY=RULY=0
LLLY=RLLY=LOWER_LEG_HEIGHT



def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glMatrixMode(GL_MODELVIEW)
  body()
  

def body():
  #TORSO
  glColor3f(1.0,1.0,1.0)
  glLoadIdentity()
  gluLookAt(0.0, 0.0, r_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
  glRotatef(TORSO_ANGLE, 0.0, 1.0, 0.0)
  
  glPushMatrix()
  glRotatef(-90, 1.0, 0.0, 0.0)
  gluCylinder(p, TORSO_RADIUS, TORSO_RADIUS, TORSO_HEIGHT, 40, 10)
  glPopMatrix()
  
  glPushMatrix()

  #HEAD
  glColor3f(0.7, 0.5, 0.5)
  glTranslatef(0.0, HEADX, 0.0)
  glRotatef(HEAD_ANGLE, 0.0, 1.0, 0.0)
  glTranslatef(0.0, HEADY, 0.0)
  glPushMatrix()

  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glScalef(0.09, 0.1, 0.1)
  glutSolidCube(1.0)
  glPopMatrix()

  #LEFT UPPER ARM
  glPopMatrix()
  glPushMatrix()
  glColor3f(0.7,0.8,0.8)
  glTranslatef(LUAX, LUAY, 0.0)
  glRotatef(LUA_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #LEFT LOWER ARM
  glColor3f(0.7,0.5,0.5)
  glTranslatef(0.0, LLAY, 0.0)
  glRotatef(LLA_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #RIGHT UPPER ARM
  glPopMatrix()
  glPushMatrix()
  glColor3f(0.7,0.8,0.8)
  glTranslatef(RUAX, RUAY, 0.0)
  glRotatef(RUA_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #RIGHT LOWER ARM
  glTranslatef(0.0, RLAY, 0.0)
  glRotatef(RLA_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glColor3f(0.7,0.5,0.5)
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #LEFT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  glColor3f(0.1,0.4,0.5)
  glTranslatef(LULX, LULY, 0.0)
  glRotatef(LUL_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #LEFT LOWER LEG

  glColor3f(0.7,0.5,0.5)
  glTranslatef(0.0, LLLY, 0.0)
  glRotatef(LLL_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #RIGHT UPPER LEG
  glPopMatrix()
  glPushMatrix()

  glColor3f(0.1,0.4,0.5)
  glTranslatef(RULX, RULY, 0.0)
  glRotatef(RUL_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  #RIGHT LOWER LEG
  glColor3f(0.7,0.5,0.5)
  glTranslatef(0.0, RLLY, 0.0)
  glRotatef(RLL_ANGLE, 1.0, 0.0, 0.0)
  
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

  glPopMatrix()
  glFlush()

  

def keypress(key, x, y):
  global TORSO_ANGLE, t1, HEAD_ANGLE, LUA_ANGLE, LLA_ANGLE, RUA_ANGLE, RLA_ANGLE
  global LUL_ANGLE, LLL_ANGLE, RUL_ANGLE, RLL_ANGLE, r_x, r_z, angle, flag
  if key == 'w':
    #Left First
    if flag == 1:            
       LUA_ANGLE = LUA_ANGLE - 10.0
       #LLA_ANGLE = LLA_ANGLE - 2.0
       RUL_ANGLE = RUL_ANGLE - 10.0
       #RLL_ANGLE = RLL_ANGLE + 4.0

       RUA_ANGLE = RUA_ANGLE + 10
       #RLA_ANGLE = LLA_ANGLE - 3.0
       LUL_ANGLE = LUL_ANGLE + 10.0
       #LLL_ANGLE = LLL_ANGLE + 6
       if LUA_ANGLE == 140:
           flag = 0
    elif flag == 0:
       LUA_ANGLE = LUA_ANGLE + 10.0
       #LLA_ANGLE = LLA_ANGLE + 2.0
       RUL_ANGLE = RUL_ANGLE + 10.0
       #RLL_ANGLE = RLL_ANGLE - 4.0

       RUA_ANGLE = RUA_ANGLE - 10
       #RLA_ANGLE = LLA_ANGLE + 3.0
       LUL_ANGLE = LUL_ANGLE - 10.0
       #LLL_ANGLE = LLL_ANGLE - 6 
       if LUA_ANGLE == 220:   
            flag = 1

  if key=='e': # TORSO
    TORSO_ANGLE = TORSO_ANGLE + 5.0
  elif key=='E':
    TORSO_ANGLE = TORSO_ANGLE - 5.0
  elif key=='s':
    LLA_ANGLE = LLA_ANGLE + 5.0
  elif key=='S':
    LLA_ANGLE = LLA_ANGLE - 5.0
  elif key=='d':
    RLA_ANGLE = RLA_ANGLE + 5.0
  elif key=='D':
    RLA_ANGLE = RLA_ANGLE - 5.0
  elif key=='f':
    LLL_ANGLE = LLL_ANGLE + 5.0
  elif key=='F':
    LLL_ANGLE = LLL_ANGLE - 5.0
  elif key=='g':
    RLL_ANGLE = RLL_ANGLE + 5.0
  elif key=='G':
    RLL_ANGLE = RLL_ANGLE - 5.0
  elif key=='r': # HEAD 
    HEAD_ANGLE = HEAD_ANGLE + 10.0
  elif key=='R':
    HEAD_ANGLE = HEAD_ANGLE - 10.0
  elif key=='t' and r_z >= 1: #Zoom
    r_z = r_z - 0.5
  elif key=='T' and r_z <= 8 :
    r_z = r_z + 0.5
  elif key=='q':
    sys.exit()

  glutPostRedisplay()
    
glutInit( sys.argv )
glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize( 800, 600 )
glutInitWindowPosition(0,0)
glutCreateWindow( 'Humanoid' )
glutDisplayFunc( display )
glutKeyboardFunc(keypress)
p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_LINE)
glClearColor(0.0, 0.0, 0.1, 0.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(30, 1.0, 0.0, 100.0)
glutMainLoop()
