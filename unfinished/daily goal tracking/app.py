from flask import Flask, render_template
from configparser import ConfigParser
import psycopg2

app = Flask(__name__)

#config parser module for creating simple config file
def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in {filename}")
    return db_params

try:
    db_config = config()
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    print("Connected to the PostgreSQL database successfully!")

    # Execute SQL queries here

except psycopg2.Error as error:
    print(f"Error: {error}")
finally:
    cursor.close()
    conn.close()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS daily_tracking (
        id SERIAL PRIMARY KEY,
        wakeup_time VARCHAR(10),
        levothyroxine_time VARCHAR(10),
        concerta_time VARCHAR(10),
        brush_teeth VARCHAR(3),
        study_hours INTEGER,
        jog_steps VARCHAR(3),
        posture_exercises VARCHAR(3),
        yoga VARCHAR(3),
        water_intake_goal VARCHAR(3),
        eat_schedule VARCHAR(3),
        project_work VARCHAR(3),
        lunch TEXT,
        dinner TEXT,
        weight VARCHAR(5)
    );
    '''

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