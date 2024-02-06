from flask import Flask, render_template
import psycopg2
from config import configuration

app = Flask(__name__)

# try to connect to PostgreSQL database
try:
    print('trying')
    conn = psycopg2.connect(
        dbname=configuration['dbname'],
        user=configuration['username'],
        password=configuration['password'],
        host=configuration['ip_address'],  # Replace with your actual host
        port=configuration['port']
    )
    print("Connected to the PostgreSQL database successfully!")
except psycopg2.Error as error:
    print(f"Error: {error}")

#check if database exists, if it doesn't create it

@app.route('/')
def index():
    print('trying', flush=True)
    return render_template('index.html')

@app.route('/create')
def create():
    print('create')

@app.route('/read')
def read():
    print('read')

@app.route('/update')
def update():
    print('update')

@app.route('/delete')
def delete():
    print('delete')

#CREATE
#READ
#UPDATE
#DELETE
#CHART DATA
    
if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=6690,
    debug=True
)