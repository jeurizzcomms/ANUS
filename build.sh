#!/usr/bin/env bash
# This is the build script for Render deployment

# Exit on error
set -o errexit

# Verwijder onnodige dependencies
pip uninstall -y playwright streamlit langchain openai anthropic

# Installeer alleen de core dependencies
pip install -r requirements.txt

# Valideer installatie
echo "Validating dependencies..."
python -c "import yaml; print('YAML dependency validated')"
python -c "import fastapi; print('FastAPI dependency validated')"
python -c "import uvicorn; print('Uvicorn dependency validated')"

# Installeer het package
pip install -e .

# Maak het script uitvoerbaar
chmod +x build.sh 