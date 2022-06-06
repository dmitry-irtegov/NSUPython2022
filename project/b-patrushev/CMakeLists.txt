cmake_minimum_required(VERSION 3.12)
project(Mandelbrot)

set(CMAKE_CXX_STANDARD 14)
add_library(Mandelbrot SHARED Mandelbrot.c)