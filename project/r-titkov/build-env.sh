#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    apt-get update
    apt-get install cmake g++ python3-venv python3-pip python3-tk -y
fi
if [ ! -d "mandelbrotEnv" ]; then
    python3 -m venv mandelbrotEnv
    mandelbrotEnv/bin/python3 -m pip install -U Pillow==9.1.1
fi
