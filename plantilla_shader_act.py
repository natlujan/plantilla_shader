from ctypes import c_void_p
import OpenGL.GL as gl
import glfw
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

vertex_shader_source = """#version 330 core
                          layout (location = 0) in vec3 position;
                          //hay que establecer posicion en la propiedad
                          //gl_Position que es del tipo vec4
                          void main() {
                            gl_Position = vec4(position.x, position.y,
                                position.z, 1.0);
                          }"""

fragment_shader_source = """#version 330 core
                            out vec4 fragmentColor;
                            void main() {
                                fragmentColor = vec4(1.0f, 0.2f, 0.1f, 1.0);
                            }"""

def main():
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

    #vertex shader
    vertex_shader = gl.glCreateShader(gl.GL_VERTEX_SHADER)
    gl.glShaderSource(vertex_shader, vertex_shader_source)
    gl.glCompileShader(vertex_shader)

    success = gl.glGetShaderiv(vertex_shader, gl.GL_COMPILE_STATUS)
    if not success:
        info_log = gl.glGetShaderInfoLog(vertex_shader)
        raise Exception(info_log)
    
    #fragment shader
    fragment_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
    gl.glShaderSource(fragment_shader, fragment_shader_source)
    gl.glCompileShader(fragment_shader)

    success = gl.glGetShaderiv(fragment_shader, gl.GL_COMPILE_STATUS)
    if not success:
        info_log = gl.glGetShaderInfoLog(fragment_shader)
        raise Exception(info_log)
    
    #Adjuntar shaders al programa de shader
    shader_program = gl.glCreateProgram()
    gl.glAttachShader(shader_program, vertex_shader)
    gl.glAttachShader(shader_program, fragment_shader)

    #Vincular el programa con openGL
    gl.glLinkProgram(shader_program)
    success = gl.glGetProgramiv(shader_program, gl.GL_LINK_STATUS)
    if not success:
        info_log = gl.glGetProgramInfoLog(shader_program, 512, None)
        raise Exception(info_log)
    
    gl.glDeleteShader(vertex_shader)
    gl.glDeleteShader(fragment_shader)

    vertices = np.array(
        [
            -0.15,-0.5,0.0,  #izquierda, abajo
            0.0, 0.5, 0.0,  #arriba
            0.5, -0.5, 0.0  #derecha
        ], dtype="float32"
    )

    #Generar vertex array object y vertex buffer object
    VAO = gl.glGenVertexArrays(1)
    VBO = gl.glGenBuffers(1)

    #Le decimos a OpenGL con cual VAO trabajar
    gl.glBindVertexArray(VAO)
    #Le decimos a OpenGL con cual Buffer trabajar
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
    #Establecerle la información al buffer
    gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, 
        gl.GL_STATIC_DRAW)
    #Definir como leer el VAO y activarlo
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, 
        gl.GL_FALSE, 0, c_void_p(0))
    gl.glEnableVertexAttribArray(0)

    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
    gl.glBindVertexArray(0)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.3,0.3,0.3,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        #Establecer que programa de shader se usa
        gl.glUseProgram(shader_program)
        #EStablecer que VAO se va a usar
        gl.glBindVertexArray(VAO)
        #Mandar a dibujar el VAO
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        gl.glBindVertexArray(0)
        gl.glUseProgram(0)

        glfw.swap_buffers(window)
        glfw.poll_events()

    gl.glDeleteVertexArrays(1, VAO)
    gl.glDeleteBuffers(1, VBO)
    gl.glDeleteProgram(shader_program)

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()
