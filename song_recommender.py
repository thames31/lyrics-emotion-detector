from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder='template')

en_songs = pd.read_csv('data/en_songs3.csv')
distance = pd.read_csv('data/distances.csv')

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
    
    links = []
    
    inpt_song = name
    dl = distance.sort_values(by=inpt_song)
    
    idx = list(dl.head(5).index)
    song_names = list(en_songs.iloc[idx]['track_name'])
    song_artists = list(en_songs.iloc[idx]['track_artist'])
    ids = list(dl.head(5).id)
    
    for id in ids:
        link = "https://open.spotify.com/track/" + id
        links.append(link)
    
    return(render_template('recommend.html', input=name,
                        link1=links[0], song1=song_names[0], artist1=song_artists[0],
                        link2=links[1], song2=song_names[1], artist2=song_artists[1],
                        link3=links[2], song3=song_names[2], artist3=song_artists[2],
                        link4=links[3], song4=song_names[3], artist4=song_artists[3],
                        link5=links[4], song5=song_names[4], artist5=song_artists[4])
) 

if __name__ == "__main__":
    app.run(debug=True,port=8080)
