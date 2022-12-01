import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import pairwise_distances

stopwords = nltk.corpus.stopwords.words('english')



def clean_lyrics(text):
    # Lowering string
    text = text.str.lower()

    # Removing non-alpha chars
    text = text.str.replace('[^a-z]', ' ')

    # Removing stopwords
    text = text.apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    

def plot_elbow(X,start,end):
    
    distortions = []
    cluster_range = range(start,end)
    
    for n_cluster in cluster_range:
        kmean_model = KMeans(n_clusters=n_cluster)
        kmean_model.fit(X)
        distortions.append(kmean_model.inertia_)
    
    plt.figure(figsize=(16,8))
    plt.plot(cluster_range, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('Elbow Method for optimal K')
    plt.show()
    
def reduce_size(matrix):
    np.fill_diagonal(matrix, matrix.max() + 5)
    rounded_matrix = np.round(matrix,2)
    return rounded_matrix

def recommend(song_id, df1, df2):
    dl = df1.sort_values(by=song_id)
    
    ids = list(dl.head(5).id)
    links = []
    
    idx = list(dl.head(5).index)
    song_names = list(df2.iloc[idx]['track_name'])
    song_artists = list(df2.iloc[idx]['track_artist'])
    
    for id in ids:
        link = "https://open.spotify.com/track/" + id
        links.append(link)
    
    return links, song_names, song_artists
