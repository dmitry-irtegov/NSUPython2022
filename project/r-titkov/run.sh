if [[ "$OSTYPE" == "darwin"* ]]; then
    OS='MAC_OS'
    if [[ "$HOSTTYPE" == "arm64" ]]; then
        LIB_NAME='mandelbrotMacOS_Arm64.so'
    elif [[ "$HOSTTYPE" == "x86_64" ]]; then
        LIB_NAME='mandelbrotMacOS_x86_64.so'
    fi
elif [[ "$OSTYPE" == "linux"* ]]; then
    OS='LINUX'
    if [[ "$HOSTTYPE" == "aarch64" ]]; then
        LIB_NAME='mandelbrotLinux_Aarch64.so'
    elif [[ "$HOSTTYPE" == "x86_64" ]]; then
        LIB_NAME='mandelbrotLinux_x86_64.so'
    fi
else
    echo "Unsupported platform!" $OSTYPE $HOSTTYPE
    exit
fi


if [ ! -d "mandelbrotEnv" ]; then
    if [[ "$OS" == "MAC_OS" ]]; then
        brew install python@3.8
        brew install python-tk
    else 
        sudo apt-get install python3.8
        sudo apt install python3-pip -y
        sudo apt-get install python3-tk -y
    fi
    wget -nc https://bootstrap.pypa.io/virtualenv/3.8/virtualenv.pyz
    python3 virtualenv.pyz mandelbrotEnv --reset-app-data
    mandelbrotEnv/bin/python3 -m pip install --upgrade pip
    mandelbrotEnv/bin/python3 -m pip install -U Pillow
fi

mandelbrotEnv/bin/python3 main.py $LIB_NAME