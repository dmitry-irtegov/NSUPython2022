#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  apt-get -y install g++ python3-venv python3-distutils python3-tk
fi

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install . -r requirements.txt
