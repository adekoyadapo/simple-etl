# ETL using Docker, Python, and MongoDB

This project demonstrates an Extract, Transform, Load (ETL) process for a LEGO database, extracting data from a PostgreSQL database using Python and loading it into MongoDB.

## Setup

### Prerequisites

- Docker
- Conda (for Python environment management)

### Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/adekoyadapo/simple-etl
   cd simple-etl
   ```

2. **Run the setup script (`deploy.sh`):**

   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```
   
   This deploys the demo and waits for 120s before removing the deployment

3. **Run with the `Makefile`:**

   ```bash
   make help # To list the make commands to run
   make all # runs the entire setup
   ./deploy.sh
   ```

## Demo Instructions

1. Ensure Docker and Conda are installed on your system.
2. Clone this repository and navigate to the project directory.
3. Run the setup script (`deploy.sh`) to download the sample database, start Docker containers, and execute the ETL process.
4. Wait for the process to complete.
5. Verify the data in MongoDB collections.

## Project Structure

- `etl.py`: Python script for ETL process.
- `requirements.txt`: List of Python dependencies.
- `docker-compose.yml`: Docker Compose configuration for PostgreSQL and MongoDB containers.
- `Makefile`: Makefile for automating the setup and execution.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Project documentation (this file).

## Author

[Ade Adekoya](https://github.com/adekoyadapo)
