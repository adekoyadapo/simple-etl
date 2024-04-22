#!/bin/bash

# Download sample db
mkdir -p data
cd data
wget -O lego.sql https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/lego.sql

cd ..
docker compose up -d

# setup python environment with pyenv

conda create -n etl python=3.11 --yes
conda run -n etl pip install -r requirements.txt
conda run -n etl python etl.py

sleep 120
# remove and cleanup
docker compose down -v --rmi all
conda remove -n etl --all --yes && conda clean -a -y