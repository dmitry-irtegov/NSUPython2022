#/usr/bin/env bash

if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "unknown os, exiting..."
    exit 1
fi

sudo apt update || exit 1
sudo apt install -y build-essential cmake || exit 1
sudo apt install -y python3 python3-pip python3-dev python3-venv
sudo apt install -y libmkl-tbb-thread libtbb-dev libtbb2

cmake_bin="./c++/build"
cmake_source="./c++/"

mkdir -p "${cmake_bin}"
cmake -S "${cmake_source}" -B "${cmake_bin}" || exit 1
cmake --build "${cmake_bin}" --clean-first

ln -sf ./c++/build/mandelbrot.so ./mandelbrot.so  || exit 1

python3 -m venv ./venv || exit 1
source ./venv/bin/activate

python3 -m pip install -r requirements.txt
