if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  apt-get -y install cmake g++ python3.8-venv python3.8-dev python3.8-tk
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install 'Pillow~=9.1.1'
