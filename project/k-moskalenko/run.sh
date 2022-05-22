python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade Pillow

mkdir build
cd build || exit

cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --clean-first

cd ../src || exit
python3 -m python
