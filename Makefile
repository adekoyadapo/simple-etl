.PHONY: help download_db start_containers setup_python_env run_etl cleanup_containers cleanup_python_env cleanup

# Help target to display available targets and their descriptions
help:
	@echo "Simple ETL Makefile"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@echo "  help                  Display this help message"
	@echo "  download_db           Download the sample database"
	@echo "  start_containers      Start Docker containers"
	@echo "  setup_python_env      Set up the Python environment"
	@echo "  run_etl               Run the ETL process"
	@echo "  cleanup_containers    Stop and remove Docker containers"
	@echo "  cleanup_python_env    Remove the Conda environment"
	@echo "  all                   Run the entire deployment"
	@echo "  cleanup               Remove the entire environment"

download_db:
	mkdir -p data
	cd data && wget -O lego.sql https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/lego.sql

start_containers:
	docker compose up -d

setup_python_env:
	cp .env.example .env
	conda create -n etl python=3.11 --yes
	conda run -n etl pip install -r requirements.txt

run_etl:
	conda run -n etl python etl.py

cleanup_containers:
	docker compose down -v --rmi all

cleanup_python_env:
	conda remove -n etl --all --yes && conda clean -a -y && rm -rf .env data

cleanup: cleanup_containers cleanup_python_env


all: download_db start_containers setup_python_env run_etl

.DEFAULT_GOAL := help