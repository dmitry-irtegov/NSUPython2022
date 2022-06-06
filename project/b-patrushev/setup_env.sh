#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  sudo apt update
  sudo apt install -y python3-pip python3-venv python3-tk
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

