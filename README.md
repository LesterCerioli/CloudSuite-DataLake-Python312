# Data Migration from PostgreSQL to Azure Data Lake Using Python 3.12

This project performs data migration from a PostgreSQL database to Azure Data Lake using Python 3.12. It connects to a PostgreSQL database, extracts the data, and uploads it to an Azure Data Lake Storage (ADLS) account.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Migration](#running-the-migration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.12
- PostgreSQL (with access to the database you want to migrate)
- Azure Data Lake Storage Gen2
- Azure Storage SDK for Python (`azure-storage-blob`)

You will also need:

- Access to the PostgreSQL database (credentials, hostname, database name).
- An Azure account with access to a Data Lake instance (account name, key, and container).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/data-lake-migration.git
   cd data-lake-migration ```bash
2. **Create and activate a virtual environment:**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate    
   venv\Scripts\activate```bash
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt```bash
4. **Configuration**
   ###### The project requires configuration values for both PostgreSQL and Azure Data Lake connections. You can set these in a config.py file or pass them as environment variables.
   ```bash
   # PostgreSQL Config
   POSTGRESQL_HOST = 'your_postgres_host'
   POSTGRESQL_DB = 'your_database'
   POSTGRESQL_USER = 'your_username'
   POSTGRESQL_PASSWORD = 'your_password'

   # Azure Data Lake Config
   AZURE_STORAGE_ACCOUNT_NAME = 'your_storage_account_name'
   AZURE_STORAGE_ACCOUNT_KEY = 'your_storage_account_key'
   AZURE_STORAGE_CONTAINER_NAME = 'your_container_name
### Running the Migration
1. **Run the Flask API:**
   ```bash
   python app.py
2. **Trigger the Migration:**
   ##### Once the API is running, you can trigger the migration by sending a POST request to the /migrate endpoint:
   ```bash
   curl -X POST http://localhost:5000/migrate

   


### Licenses

### Key Elements Explained:
1. **Prerequisites**: Lists the required software and services.
2. **Installation**: Instructions for setting up the project, including virtual environments and dependencies.
3. **Project Structure**: Clear breakdown of the project’s directory and files.
4. **Configuration**: Guides the user on how to configure PostgreSQL and Azure Data Lake connection parameters.
5. **Running the Migration**: Shows how to run the Flask app and trigger the migration.
6. **Error Handling**: Explains how errors are captured and logged.
7. **Contributing**: Invites contributions and issues from other developers.




  
    

