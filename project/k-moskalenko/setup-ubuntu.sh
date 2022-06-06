#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  sudo apt update
  sudo apt install -y python3-pip python3-dev python3-venv python3-tk
fi
