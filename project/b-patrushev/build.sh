#!/usr/bin/env bash
gcc Mandelbrot.c -fopenmp -fPIC -shared -o Mandelbrot.so
