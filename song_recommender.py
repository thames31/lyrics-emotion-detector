from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def get_input():
    if request.method == 'POST':
        song = request.form['song_name']
        return redirect(url_for('recommend', name=song))

@app.route('/recommend/<name>')
def recommend(name):
    return("You should listen to https://open.spotify.com/track/385Urz8Qa8CIcK9tl3SA8g" )

if __name__ == "__main__":
    app.run(debug=True,port=8080)
