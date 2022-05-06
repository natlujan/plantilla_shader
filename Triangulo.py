from Modelo import *
import glm 

class Triangulo(Modelo):

    def __init__(self, shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.vertices = np.array(
            [
                -0.15, -0.5, 0.0,1.0 ,  1.0, 0.0, 0.0, 1.0,  # Izquierda, abajo
                0.0, 0.5, 0.0,1.0    ,  1.0, 0.0, 0.0, 1.0,  # Arriba
                0.5, -0.5, 0.0,1.0 ,    1.0, 0.0, 0.0, 1.0   # Derecha
            ], dtype = "float32"
        )
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones, glm.vec3(0.5,-0.2,0.0))
        self.transformaciones = glm.rotate(self.transformaciones, 45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.ARRIBA:
            cantidad_movimiento.y = cantidad_movimiento.y + 0.05
        elif direccion == self.ABAJO:
            cantidad_movimiento.y = cantidad_movimiento.y - 0.05

        self.transformaciones
