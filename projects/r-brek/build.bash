#/usr/bin/env bash

cmake_bin="./c++/build"
cmake_source="./c++/"

mkdir -p "${cmake_bin}"
cmake -S "${cmake_source}" -B "${cmake_bin}" || exit 1
cmake --build "${cmake_bin}" --clean-first

ln -sf ./c++/build/mandelbrot.so ./mandelbrot.so  || exit 1
