from distutils.core import setup, Extension

module = Extension('mandlebrotLib',
                    sources = ['cppmult.cpp'],
						  language = "c++",
						  extra_compile_args=['-std=c++11'])

setup (name = 'mandlebrotLib',
       version = '1.0',
       ext_modules = [module])