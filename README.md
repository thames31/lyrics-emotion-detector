# Information 

This project's initial goal is to build a recommendation system that will select the top 5 songs similar to an inputted song. Because sometimes we get bored of listening to the same one song that we love. In order to prevent such tragedy from happening, we should listen to other songs that are similar to our beloved song.

The dataset that we will be using is available on [Kaggle](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs). It contains over 18000 Spotify songs along with musical features such as danceability, tempo, loudness etc... For this project, we will however, only use lyrical content of each songs in English. In the future we could look at songs of other languages and incorporate them into our recommendation system.

# Tools used for this project

Python (Pandas, numpy, matplotlib) Flask, HTML, CSS

# Exploratory Data Analysis

The very first thing that has to be done is to make sure that the dataset is cleaned and ready to be used. In the dataset, an observation can be made that a lot of songs had the same track name and artist but different album. This problem could be solved by creating a new column which would be a string concatenation of the artist name and the track name. Next, we can start by dropping every duplicates but keeping at least one iteration of the song.

In order to work with the lyrics, we need to remove non alphanumeric characters (foreign language characters such as Korean alphabets), lowering the case of each words and removing stopwords in the English language.

# Clustering the dataset

After we are done cleaning the data, we can then use SK-Learn tfidfVectorizer to create NLP features for our dataset. We can then use KMeans and the elbow method to cluster each songs based on their lyrics.

Second clustering will be performed based on the new cluster labels and other musical features from the original dataset:
- danceability
- energy
- speechiness
- acousticness
- tempo
- instrumentalness

# Designing the recommendation system

SK-Learn's pairwise distance was used to calculate the euclidean distance between each data point. We can now sort by ascension based on one song and we would get the songs that are closest to our target. 

# Deployment

Unfortunately, an important csv file could not be pushed into the repository since it was 1GB. If you wish to see the deployment on your local machine, you need to run these notebooks in the following order to generate the important csv file for the recommendation algorithm. 

**Make sure to open distance.ipynb and check that the last cell is uncommented so the dataframe is converted to a csv file.**

1. distance.ipynb (distances.csv file should be generated in the data folder)
2. deployment.ipynb

After you have ran both of these notebooks, you can now run ``` python song_recommender.py``` in your terminal. 

 **Make sure that the terminal is in the same directory as the repository.**


# Contact Me

Thames Manisy - [My Discord](https://discord.com/channels/Thames#7138) - thamesmanisy@gmail.com

Project Link: [Song Recommender](https://github.com/thames31/lyrics-emotion-detector)



