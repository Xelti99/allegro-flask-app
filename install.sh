#!/bin/bash

# Tworzenie wirtualnego środowiska
python3 -m venv venv

# Aktywacja wirtualnego środowiska
source venv/bin/activate

# Instalacja zależności
pip install -r requirements.txt
