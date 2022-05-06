#version 330 core
//Los in vienen del vertex shader y no del CPU
in vec4 fragmentColor;
//Los out, van hacia el buffer
out vec4 outFragmentColor;
void main() {
    outFragmentColor = fragmentColor;
}
