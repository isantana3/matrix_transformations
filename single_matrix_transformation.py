from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def eixoXY():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-300, 0)
    glVertex2f(300, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -300)
    glVertex2f(0, 300)
    glEnd()


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300.0, 300, -300.0, 300, -300.0, 300.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def triangle(r, g, b):
    glBegin(GL_TRIANGLES)
    glColor3f(r, g, b)
    glVertex2f(-100.0, -100.0)
    glColor3f(r, g, b)
    glVertex2f(100.0, -100.0)
    glColor3f(r, g, b)
    glVertex2f(0.0, 100.0)
    glEnd()


def display():
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    triangle(1.0, 0.0, 0.0)
    glLoadIdentity()
    # rotação dem 30º, translação(-150x, 100y) e escala (50%)
    matrix = np.array(
        [
            0.075,  # (cos 30º)/2
            -0.5,  # (-sin 30º)/2
            0.0,
            0.0,
            0.5,  # (sin 30º)/2
            0.075,  # (cos 30º)/2
            0.0,
            0.0,
            0.0,
            0.0,
            0.5,  # 50%z
            0.0,
            -150.0,  # 150px rith
            100.0,  # 100px top
            0.0,
            1.0,
        ]
    )
    glLoadMatrixf(matrix)
    triangle(0.0, 0.0, 1.0)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(-300, -300)
    glutCreateWindow('triangle')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    # note need to do this to properly render faceted geometry
    glutMainLoop()


if __name__ == "__main__":
    main()
