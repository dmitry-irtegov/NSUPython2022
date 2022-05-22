conda env create -f env.yml
g++ -O3 -shared -std=c++11 -fPIC cppmult.cpp -o libcppmult.so 
conda run -n mandelbrot /bin/bash -c "python main.py"