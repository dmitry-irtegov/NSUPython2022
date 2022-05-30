python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install 'Pillow~=9.1.1'

mkdir build
cd build || exit

cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --clean-first
