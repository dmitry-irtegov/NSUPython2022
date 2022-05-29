# Mandelbrot set

## Linux x64/arm64 or MacOS x64/arm64

To run project on **Linux x64/arm64** or **MacOS x64/arm64**:
`./run.sh`

## Other system
On other system it is required to build c++ library:  
`g++ -O3 -shared -std=c++11 -fPIC cppmult.cpp -o mandelbrotLib.so`

Also Pillow library is required:  
`pip install -U Pillow`

Finally run project with:  
`python3 main.py mandelbrotLib.so`