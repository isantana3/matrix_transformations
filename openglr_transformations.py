from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    draw_cone(color=(1.0, 0.0, 0.0))
    # escala (50%) e translação (150x, 100y)
    glTranslated(150.0, 100.0, 0.0)
    glScaled(0.5, 0.5, 0)
    draw_cone(color=(0.0, 1.0, 0.0))

    glLoadIdentity()
    # inverte o triângulo com escala negativa no eixo y
    glScaled(1.0, -1.0, 1.0)
    draw_cone(color=(0.0, 0.0, 1.0))

    glLoadIdentity()
    # rotação dem 30º, translação(-150x, 100y) e escala (50%)
    glTranslated(-150.0, 100.0, 0.0)
    glScaled(0.5, 0.5, 0)
    glRotated(30, 0, 0, 1.0)
    draw_cone(color=(0.5, 0.5, 1.0))

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
