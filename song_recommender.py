from flask import Flask, render_template, request, redirect, url_for
from functions import *

app = Flask(__name__, template_folder='template')

distance = pd.read_csv('data/distances.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def get_input():
    if request.method == 'POST':
        song = request.form['song_name']
        artist = request.form['artist_name']
        return redirect(url_for('recommend', name = song, artist_name = artist))

@app.route('/recommend/<artist_name>/<name>')
def recommend(name, artist_name):
    
    links = recommend_songs(name, artist_name, distance)

    return(render_template('recommend.html', input=name,
                        link1=links[0],
                        link2=links[1],
                        link3=links[2],
                        link4=links[3],
                        link5=links[4])
) 

if __name__ == "__main__":
    app.run(debug=True,port=8080)
