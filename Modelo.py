import OpenGL.GL as gl
import numpy as np
from ctypes import c_void_p
import glm

class Modelo:
    def __init__(self, shader, posicion_id, color_id, transformaciones_id):
        self.shader = shader
        self.transformaciones_id = transformaciones_id

        #Generar vertex array object y vertex buffer object
        self.VAO = gl.glGenVertexArrays(1)
        self.VBO = gl.glGenBuffers(1)

        #Le decimos a OpenGL con cual VAO trabajar
        gl.glBindVertexArray(self.VAO)
        #Le decimos a OpenGL con cual Buffer trabajar
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.VBO)
        #Establecerle la información al buffer
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, 
            gl.GL_STATIC_DRAW)
        #Definir como leer el VAO y activarlo
        #posicion
        gl.glVertexAttribPointer(posicion_id, 4, gl.GL_FLOAT, 
            gl.GL_FALSE, 8 * self.vertices.itemsize, c_void_p(0))
        gl.glEnableVertexAttribArray(posicion_id)
        #color
        gl.glVertexAttribPointer(color_id, 4, gl.GL_FLOAT,
            gl.GL_FALSE, 8 * self.vertices.itemsize, c_void_p(4 * self.vertices.itemsize))
        gl.glEnableVertexAttribArray(color_id)


        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        gl.glBindVertexArray(0)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id, 1, gl.GL_FALSE, 
            glm.valueptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLES,0,3)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)
        
