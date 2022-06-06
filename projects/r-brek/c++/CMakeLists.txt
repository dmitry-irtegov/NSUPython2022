cmake_minimum_required(VERSION 3.12)
project(mandelbrot)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_SHARED_MODULE_PREFIX "")

find_package(Python3 REQUIRED COMPONENTS Development)
find_package(TBB REQUIRED)

add_library(mandelbrot MODULE mandelbrot.cpp)
target_link_libraries(mandelbrot Python3::Python TBB::tbb)
# Python_add_library(mandelbrot MODULE mandelbrot.cpp)
# target_link_libraries(mandelbrot STATIC TBB::tbb)
