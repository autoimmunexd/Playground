from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#CREATE
#READ
#UPDATE
#DELETE
#CHART

#check if database exists, if it doesn't create it
#connect to the database
#check if database data structure exists

if __name__ == '__main__':
    app.run(debug=True)