from flask import Flask, render_template, redirect, request
from nosub import *

app = Flask(__name__)

@app.route('/')
def index():
    channel_subs = get_feed(subscriptions)
    print(channel_subs)
    return render_template('index.html', channel_subs=channel_subs)

@app.route('/manage')
def manage():
    names = get_subscriptions(subscriptions)
    return render_template('manage.html', names=names)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        new_sub = request.form['subscription']
        add_subscription(new_sub, subscriptions)
    return redirect('/manage')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    subscriptions = load()
    app.run(debug=True)