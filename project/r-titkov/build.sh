if [ ! -d "mandelbrotEnv" ]; then
    if [[ "$OS" == "MAC_OS" ]]; then
        brew install python@3.8
        brew install python-tk
    else 
        sudo apt-get install cmake g++ python3.8-venv python3.8-dev python3.8-tk -y
    fi
    wget -nc https://bootstrap.pypa.io/virtualenv/3.8/virtualenv.pyz
    python3 virtualenv.pyz mandelbrotEnv --reset-app-data
    mandelbrotEnv/bin/python3 -m pip install --upgrade pip
    mandelbrotEnv/bin/python3 -m pip install -U Pillow==9.1.1
fi

python setup.py build
find ./build/*/ -name "mandlebrotLib*.so" -exec mv {} "mandlebrotLib.so" \;
