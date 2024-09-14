#!/bin/bash

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Configurar la base de datos
echo "Configurando la base de datos..."
sqlite3 data/data.db < data/setup.sql

# Iniciar la aplicación
echo "Iniciando la aplicación..."
uvicorn app.main:app
