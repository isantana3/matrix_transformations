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


def draw_cone(
    color, position=(0, -1, 0), radius=100, height=200, slices=5000, stacks=1000
):
    '''Desenha um cone utilizinado o método glutSolidCone do glut como base'''
    glPushMatrix()
    try:
        glColor(color)
        glTranslatef(*position)
        glRotatef(250, 1, 0, 0)
        glutSolidCone(radius, height, slices, stacks)
    finally:
        glPopMatrix()


def display():
    glClearColor(0.5, 0.5, 0.5, 0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    draw_cone(color=(0.8, 0.1, 0.2, 0.5))
    glLoadIdentity()

    # escala (50%) e translação (150x, 100y)
    matrix_1 = np.array(
        [
            0.5,  # 50%x
            0.0,
            0.0,
            0.0,
            0.0,
            0.5,  # 50%y
            0.0,
            0.0,
            0.0,
            0.0,
            0.5,  # 50%z
            0.0,
            150.0,  # 150px rith
            100.0,  # 100px top
            0.0,
            1.0,  #
        ]
    )
    glLoadMatrixf(matrix_1)

    draw_cone(color=(1, 0, 0, 0.5))
    glLoadIdentity()

    # inverte o triângulo com escala negativa no eixo y
    matrix_2 = np.array(
        [
            1.0,  # escala eixo x
            0.0,
            0.0,
            0.0,
            0.0,
            -1.0,  # escala eixo y
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,  # escala eixo z
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
        ]
    )
    glLoadMatrixf(matrix_2)

    draw_cone(color=(0.0, 1.0, 0.0, 0.5))
    glLoadIdentity()

    # rotação dem 30º, translação(-150x, 100y) e escala (50%)
    matrix_3 = np.array(
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
    glLoadMatrixf(matrix_3)
    draw_cone(color=(0.0, 0.0, 1.0, 0.5))

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
