cmake_minimum_required(VERSION 3.12)
project(mandelbrot)

set(CMAKE_CXX_STANDARD 11)

find_package(Python COMPONENTS Development)
Python_add_library(mandelbrot cppmult.cpp cppmult.hpp cptl.h)