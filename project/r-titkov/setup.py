from setuptools import setup, Extension

module = Extension('mandelbrotLib',
                     sources = ['cppmult.cpp'],
                     language = "c++",
                     extra_compile_args=['-std=c++11'])

setup (name = 'mandelbrotLib',
       version = '1.0',
       ext_modules = [module])