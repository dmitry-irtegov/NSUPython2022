find_package(Python COMPONENTS Development)
Python_add_library(mandelbrot mandelbrot.cpp palette.h ctpl_stl.h)

add_custom_command(TARGET mandelbrot POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E create_symlink
        $<TARGET_FILE:mandelbrot>
        $<TARGET_FILE_NAME:mandelbrot>
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR})