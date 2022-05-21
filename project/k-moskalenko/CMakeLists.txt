cmake_minimum_required(VERSION 3.12)
project(mandelbrot)

set(CMAKE_CXX_STANDARD 14)

find_package(Python COMPONENTS Development)
Python_add_library(mandelbrot mandelbrot.cpp)

add_custom_command(TARGET mandelbrot POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E create_symlink
        $<TARGET_FILE:mandelbrot>
        $<TARGET_FILE_NAME:mandelbrot>
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
