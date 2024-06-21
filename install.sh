#!/bin/bash

# Tworzenie wirtualnego środowiska
python3 -m venv venv
if [ $? -ne 0 ]; then
  echo "Failed to create virtual environment"
  exit 1
fi

# Aktywacja wirtualnego środowiska
source venv/bin/activate
if [ $? -ne 0 ]; then
  echo "Failed to activate virtual environment"
  exit 1
fi

# Instalacja zależności
pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Failed to install dependencies"
  exit 1
fi
