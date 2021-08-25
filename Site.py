import streamlit as st
import pandas as pd
import numpy as np
import json
from youtubesearchpython import SearchVideos # YouTube search tool
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = "11e5271cd71241ba81d4f815ff5dc232"
client_secret = "01312af2680947dd8e6a55da36bf4056"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

sp.trace=False
# Get a Song str search
def getMusicName(elem):
    return '{} - {}'.format(elem['artist'], elem['name'])


# Function to search a YouTube Video
def youtubeSearchVideo(music, results=1):
    searchJson = SearchVideos(music, offset=1, mode="json", max_results=results).result()
    searchParsed = json.loads(searchJson)
    searchParsed = searchParsed['search_result'][0]
    return {'title': searchParsed['title'], \
            'duration': searchParsed['duration'], \
            'views': searchParsed['views'], \
            'url': searchParsed['link'] }

# K-query
def knnQuery(queryPoint, df, k):
    transf = MinMaxScaler(feature_range=(0, 1), copy=True).fit(df)
    tmp = pd.DataFrame(transf.transform(df))
    scaledQueryPoint = pd.DataFrame(transf.transform(queryPoint))
    tmp['dist'] = tmp.apply(lambda x: np.linalg.norm(x-scaledQueryPoint.loc[0]), axis=1)
    tmp = tmp.sort_values('dist')
    return tmp.head(k).index

# Range query
def rangeQuery(queryPoint, arrCharactPoints, radius):
    tmp = arrCharactPoints.copy(deep=True)
    tmp['dist'] = tmp.apply(lambda x: np.linalg.norm(x-queryPoint), axis=1)
    tmp['radius'] = tmp.apply(lambda x: 1 if x['dist'] <= radius else 0, axis=1)
    return tmp.query('radius == 1').index

# Execute k-NN removing the 'query point'
# def querySimilars(df, columns, idx, func, param):
#     arr = df[columns].copy(deep=True)
#     queryPoint = arr.loc[idx]
#     arr = arr.drop([idx])
#     response = func(queryPoint, arr, param)
#     return response

# Execute k-NN, not removing eventually existing query point
def querySimilars2(df, col, queryPoint, func, param):
    response = func(queryPoint[col], df[col], param)
    return response

def dfQuery(songToSearch):
    response = sp.search(songToSearch)['tracks']['items'][0]
    
    songFeatures = {} #Creates dictionary for that specific album

    #Create keys-values dictionary for song
    songFeatures['album'] = response['album']['name']
    songFeatures['artist'] = response['album']['artists'][0]['name']
    songFeatures['track_number'] = response['track_number']
    songFeatures['id'] = response['id']
    songFeatures['name'] = response['name']
    songFeatures['uri'] = response['uri']
    
    #pull audio features per track
    features = sp.audio_features(songFeatures['uri'])

    #Append to relevant key-value
    songFeatures['acousticness'] = features[0]['acousticness']
    songFeatures['danceability'] = features[0]['danceability']
    songFeatures['energy'] = features[0]['energy']
    songFeatures['instrumentalness'] = features[0]['instrumentalness']
    songFeatures['liveness'] = features[0]['liveness']
    songFeatures['loudness'] = features[0]['loudness']
    songFeatures['speechiness'] = features[0]['speechiness']
    songFeatures['tempo'] = features[0]['tempo']
    songFeatures['valence'] = features[0]['valence']
    #popularity is stored elsewhere
    pop = sp.track(songFeatures['uri'])
    songFeatures['popularity'] = pop['popularity']
    
    df = pd.DataFrame.from_dict([songFeatures])
    
    return df
   
def Similarities(songToSearch, k=3):
    """search has to be a string, for example 'Artist - Title' """
    
    # Get audio features of the song from Spotify
    dfResult = dfQuery(songToSearch)
    
    #Select parameters for the analysis
    col = ['acousticness','danceability','energy','instrumentalness','liveness','speechiness','valence']
    dfSongs, func = pd.read_csv('final.csv'), knnQuery
    del dfSongs["Unnamed: 0"]

    similarSongs = querySimilars2(dfSongs, col, dfResult, func, k)
    
    # Select a song
    anySong = dfResult.loc[0]
    # Get the song name
    anySongName = getMusicName(anySong)
    # Retrive a YouTube link
    youtube = youtubeSearchVideo(anySongName)

    # Print
    print('# Query Point')
    print(songIndex, anySongName)
    print(youtube['url'])
    
    print('# Similar songs')
    for idx in similarSongs:
        anySong = dfSongs.loc[idx]
        anySongName = getMusicName(anySong)
        youtube = youtubeSearchVideo(anySongName)

        print(idx, anySongName)
        print(youtube['url'])   
   
   

st.title('''
   Welcome to the music recommendation system of IDF Music !      
''')

# input = ['Bal musette', 'Jazz', 'Punk', 'Rock', 'Rap',
#          'RnB', 'Dancehall/Ragga', 'Reggaeton', 'Zouglou',
#          'Coupé-décalé', 'Logoby', 'Zouk', 'Disco', 'French Touch',
#          'Turntablism/platinisme', 'Tecktonik', 'Electro', 'Folk',
#          'Jazz', 'Pop rock', 'Reggae', 'Country', 'Blues',
#          'Rock garage', 'World', 'Ska', 'Raï', 'Gypsy pop', 'Tango', 'Opérette', 'Variété']
input = ['Default', 'Rap', 'Electro', 'Rock', ]

dic = {
    'in': input,
    'out': {
        'Default': '',
        'Any song': '',
        'Rock': 'Superbus, Kyo',
        'Rap': 'Booba, Nekfeu',
        'Electro': 'David Guetta',
        'Variété': 'Vianney, Kendji Girac, GIMS'

    }
}

# user_input = st.text_input("Gimme a song", "Artist - Title")

option = st.selectbox(
    'Tell me more about you. What is your style of music?',
    dic['in'])

st.cache()
if option == 'Default':
    st.write('Choose a style !')
    
elif option == 'Any song':
    # User can write a song to search
    st.write('Write your song')
    entry = st.text_input("Enter a song to search for its similarities", "Type here ...")
    if(st.button('Submit')):
    songToSearch = str(entry)
    Similarities(songToSearch)
    
else:
    # Selection among pre-defined songs
   out = dic['out'][option]
   'Check for this: ', out
   st.write('Want to learn more about these?')



# '''Show all results as buttons'''
# liste_artistes = out.split(',')
# for artiste in liste_artistes:
#     name = st.button(artiste)


if option == 'Rap':
    Booba = st.button('Booba')
    Nekfeu = st.button('Nekfeu')
if option == 'Rap' and Booba:
    url = "https://www.youtube.com/watch?v=Stet_4bnclk"     
    st.write('Try this one: [DKR](%s)' % url)
if option == 'Rap' and Nekfeu:
    url = "https://www.youtube.com/watch?v=YltjliK0ZeA"
    st.write('This one is cool: [On verra bien](%s)' % url)

if option == 'Electro':
    DavidGuetta = st.button('David Guetta')
if option == 'Electro' and DavidGuetta:
    url = "https://www.youtube.com/watch?v=JRfuAukYTKg"
    st.write('The biggest hit is: [Titanium(ft. SIA)](%s)' % url)

if option == 'Rock':
    Kyo = st.button('Kyo')
    Superbus = st.button('Superbus')
if option == 'Rock' and Superbus:
    url = "https://www.youtube.com/watch?v=CQPNj38WscM"
    st.write('Try this: [Butterfly](%s)' % url)
if option == 'Rock' and Kyo:
    url = "https://www.youtube.com/watch?v=hWXYnW2Um68"
    st.write('This song was a hit: [Le Graal](%s)' % url)
