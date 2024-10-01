#!/bin/bash

# Instalar dependencias
echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Configurar la base de datos
echo "Configuring the database..."
sqlite3 data/data.db < data/setup.sql > /dev/null 2>&1

# Iniciar la aplicación
echo "Starting the application..."
uvicorn app.main:app
