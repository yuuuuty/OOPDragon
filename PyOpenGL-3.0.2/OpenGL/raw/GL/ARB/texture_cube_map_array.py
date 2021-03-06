'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_ARB_texture_cube_map_array'
_p.unpack_constants( """GL_TEXTURE_CUBE_MAP_ARRAY_ARB 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY_ARB 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB 0x900F""", globals())


def glInitTextureCubeMapArrayARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
