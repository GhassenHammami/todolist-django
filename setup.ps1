Write-Host "Creating virtual environment..."
python -m venv env

Write-Host "Activating virtual environment..."
.\env\Scripts\activate

Write-Host "Installing Django..."
pip install django

Write-Host "Installing project requirements..."
pip install -r requirements.txt

Write-Host "Setup complete!"