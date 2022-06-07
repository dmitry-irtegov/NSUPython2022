from distutils.core import setup
from distutils.extension import Extension

mandelbrot_module = Extension(
    name='mandelbrot',
    sources=['src/c++/mandelbrot.cpp'],
    extra_compile_args=['-std=c++14'],
)

setup(
    name='MandelbrotProject',
    version='1.0',
    author='Konstantin Moskalenko',
    author_email='kkmoskalenko@icloud.com',
    url='https://github.com/kkmoskalenko/NSUPython2022',
    ext_modules=[mandelbrot_module],
)
