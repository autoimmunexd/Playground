import subprocess
import sys

# Check if PostgreSQL is installed, and install it if necessary
def check_postgres_installed():
    try:
        subprocess.run(['psql', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("PostgreSQL is already installed.")
    except FileNotFoundError:
        print("PostgreSQL client 'psql' not found. Installing PostgreSQL.")
        install_postgres()
    except subprocess.CalledProcessError:
        print("PostgreSQL is not installed.")
        install_postgres()

# Check if the database exists, and create it if necessary
def check_postgres_database():
    try:
        subprocess.run(['su', '-', 'postgres', '-c', 'psql -c "CREATE DATABASE IF NOT EXISTS nosub_db"'], check=True)
        print('Database creation done.')
    except subprocess.CalledProcessError:
        create_database()

# Install PostgreSQL
def install_postgres():
    print("Installing PostgreSQL...")
    try:
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        # Install PostgreSQL itself
        subprocess.run(['sudo', 'apt', 'install', 'postgresql', '-y'], check=True)
        # Install psql (command line tool for working with PostgreSQL)
        subprocess.run(['sudo', 'apt', 'install', 'postgresql-client', '-y'], check=True)
        print("PostgreSQL installed successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to install PostgreSQL.")
        raise RuntimeError("Failed to install PostgreSQL")

# Create database
def create_database():
    try:
        # Write SQL script to a temporary file
        with open('/tmp/create_database.sql', 'w') as f:
            f.write('CREATE DATABASE nosub_db;')

        # Execute SQL script using psql
        subprocess.run(['su', '-', 'postgres', '-c', 'psql -f /tmp/create_database.sql'], check=True)
        print('Database creation done.')
        #lists the databases for user postgres via psql command line program/client
        subprocess.run(['su', 'postgres', '-c', 'psql -U postgres -d nosub_db -c "\\l"'], check=True)
    except subprocess.CalledProcessError as e:
        # Ignore error if database already exists
        if 'already exists' in e.stderr.decode():
            print('Database already exists.')
        else:
            print("Error: Failed to create database.")
            raise RuntimeError("Failed to create database")
    finally:
        # Clean up temporary file
        subprocess.run(['rm', '/tmp/create_database.sql'])

# Check PostgreSQL installation and database existence
check_postgres_installed()
check_postgres_database()
#su postgres
#psql -U postgres -d nosub_db
#\l