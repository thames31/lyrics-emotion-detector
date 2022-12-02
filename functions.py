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

    text = text.str.lower()
    text = text.str.replace('[^a-z]', ' ')
    text = text.apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    return text

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

def recommend_songs(song_name, artist, df):
    
    artistnsong = artist + " " + song_name

    dl = df.sort_values(by=artistnsong)
    
    ids = list(dl.head(5).id)
    links = []
    
    for id in ids:
        link = "https://open.spotify.com/embed/track/" + id + "?utm_source=generator"
        links.append(link)
    
    return links