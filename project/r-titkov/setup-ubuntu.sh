#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
   sudo apt-get update
   sudo apt-get install cmake g++ python3-venv python3-pip python3-tk -y
fi