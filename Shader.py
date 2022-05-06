import OpenGL.GL as gl

class Shader:
    def __init__(self, vertex_shader_source, fragment_shader_source):
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
        self.shader_program = gl.glCreateProgram()
        gl.glAttachShader(self.shader_program, vertex_shader)
        gl.glAttachShader(self.shader_program, fragment_shader)

        #Vincular el programa con openGL
        gl.glLinkProgram(self.shader_program)
        success = gl.glGetProgramiv(self.shader_program, gl.GL_LINK_STATUS)
        if not success:
            info_log = gl.glGetProgramInfoLog(self.shader_program, 512, None)
            raise Exception(info_log)
        
        gl.glDeleteShader(vertex_shader)
        gl.glDeleteShader(fragment_shader)

    def usar_programa(self):
        gl.glUseProgram(self.shader_program)

    def liberar_programa(self):
        gl.glUseProgram(0)

    def borrar(self):
        gl.glDeleteProgram(self.shader_program)
        
