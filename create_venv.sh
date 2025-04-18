#!/bin/bash

# Set the virtual environment name
VENV_NAME="economics"

# Check if the virtual environment already exists
if [ -d "/usr/local/bin/$VENV_NAME" ]; then
  echo "Virtual environment '$VENV_NAME' already exists."
else
  # Create the virtual environment
  python3 -m venv "/usr/local/bin/$VENV_NAME"
  
  if [ $? -eq 0 ]; then
    echo "Virtual environment '$VENV_NAME' created successfully."
  else
    echo "Failed to create virtual environment '$VENV_NAME'."
    exit 1
  fi
fi
