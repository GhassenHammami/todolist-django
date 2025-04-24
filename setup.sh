#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv env

echo "Activating virtual environment..."
source env/bin/activate

echo "Installing Django..."
pip install django

echo "Installing project requirements..."
pip install -r requirements.txt

echo "Setup complete!"