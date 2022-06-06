#!/bin/bash

if [ ! -d "mandelbrotEnv" ]; then
    python3 -m venv mandelbrotEnv
    mandelbrotEnv/bin/python3 -m pip install -U Pillow==9.1.1
fi
