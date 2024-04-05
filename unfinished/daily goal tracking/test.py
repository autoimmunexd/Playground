import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'journal2',
    'user': 'posty',
    'password': 'password',
    'host': 'localhost',  # Use 'localhost' for local connection
    'port': '5432'        # Default PostgreSQL port
}

try:
    # Establish a connection to the PostgreSQL server
    with psycopg2.connect(**db_params) as conn:
        # Create a cursor object to execute SQL queries
        with conn.cursor() as cursor:
            # Example query: Select version information from the server
            cursor.execute('SELECT version();')
            version = cursor.fetchone()

            print(f'Connected to the PostgreSQL server. Server version: {version[0]}')

except psycopg2.Error as e:
    print(f'Error: {e}')

# This part will execute even if an exception occurs, ensuring that the connection is closed.
finally:
    print('Connection closed.')