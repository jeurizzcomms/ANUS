#!/usr/bin/env bash
# This is the build script for Render deployment

# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Make the script executable
chmod +x build.sh 