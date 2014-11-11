'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_ATI_texture_float'
_p.unpack_constants( """GL_RGBA_FLOAT32_ATI 0x8814
GL_RGB_FLOAT32_ATI 0x8815
GL_ALPHA_FLOAT32_ATI 0x8816
GL_INTENSITY_FLOAT32_ATI 0x8817
GL_LUMINANCE_FLOAT32_ATI 0x8818
GL_LUMINANCE_ALPHA_FLOAT32_ATI 0x8819
GL_RGBA_FLOAT16_ATI 0x881A
GL_RGB_FLOAT16_ATI 0x881B
GL_ALPHA_FLOAT16_ATI 0x881C
GL_INTENSITY_FLOAT16_ATI 0x881D
GL_LUMINANCE_FLOAT16_ATI 0x881E
GL_LUMINANCE_ALPHA_FLOAT16_ATI 0x881F""", globals())


def glInitTextureFloatATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )