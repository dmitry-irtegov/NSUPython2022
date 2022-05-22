mkdir build
cd build || exit

cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --clean-first

cd ../src || exit
python -m python
