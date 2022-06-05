#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  apt update
  apt install -y python3-pip python3-dev python3-venv python3-tk
fi

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install . -r requirements.txt
