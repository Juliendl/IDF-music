import streamlit as st
import pandas as pd
import numpy as np

st.title('''
   Welcome to the music recommendation system of IDF Music !      
''')

# input = ['Bal musette', 'Jazz', 'Punk', 'Rock', 'Rap',
#          'RnB', 'Dancehall/Ragga', 'Reggaeton', 'Zouglou',
#          'Coupé-décalé', 'Logoby', 'Zouk', 'Disco', 'French Touch',
#          'Turntablism/platinisme', 'Tecktonik', 'Electro', 'Folk',
#          'Jazz', 'Pop rock', 'Reggae', 'Country', 'Blues',
#          'Rock garage', 'World', 'Ska', 'Raï', 'Gypsy pop', 'Tango', 'Opérette', 'Variété']
input = ['No choice', 'Rap', 'Electro', 'Rock', ]

dic = {
    'in': input,
    'out': {
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
