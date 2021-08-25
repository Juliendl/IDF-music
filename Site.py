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
input = ['Default', 'Rap', 'Electro', 'Rock', ]

dic = {
    'in': input,
    'out': {
        'Default': '',
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
else:
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
    url1 = "https://www.youtube.com/watch?v=Stet_4bnclk"
    url2 =  "https://www.youtube.com/watch?v=R3VhomP5b10"
    url3 = "https://www.youtube.com/watch?v=hwtLqJyhS3Q"
    url4 =  "https://www.youtube.com/watch?v=OXewKWKvva8"
    url5 =  "https://www.youtube.com/watch?v=s4JbpWWV8sM&pp=sAQA"
    st.write('These ones are among the biggest hits: [DKR](%s)' % url1, ', [Habibi](%s)' % url2, ', [92i Veyron](%s)' % url3, ', [Pinocchio(ft. Damso & Gato)](%s)' % url4, ', [Comme une étoile](%s)' % url5)
if option == 'Rap' and Nekfeu:
    url1 = "https://www.youtube.com/watch?v=YltjliK0ZeA&pp=sAQA"
    url2 =  "https://www.youtube.com/watch?v=Z68u6dJqoI0&pp=sAQA"
    url3 = "https://www.youtube.com/watch?v=cBKGKkQnI94"
    url4 =  "https://www.youtube.com/watch?v=V_S-bDdY1lA"
    url5 =  "https://www.youtube.com/watch?v=eZC2Ohdk-wI"
    st.write('These ones are among the biggest hits: [On verra bien](%s)' % url1, ', [Ma Dope(ft. SPri Noir)](%s)' % url2, ', [Elle pleut(ft. Nemir)](%s)' % url3, ', ["Le regard des gens(ft. Nemir, 2zer, Mekra, Doums)"](%s)' % url4, ', [Cheum](%s)' % url5)

if option == 'Electro':
    DavidGuetta = st.button('David Guetta')
if option == 'Electro' and DavidGuetta:
    url1 = "https://www.youtube.com/watch?v=JRfuAukYTKg"
    url2 =  "https://www.youtube.com/watch?v=NUVCQXMUVnI"
    # url3 = "https://www.youtube.com/watch?v=cBKGKkQnI94"
    # url4 =  "https://www.youtube.com/watch?v=V_S-bDdY1lA"
    # url5 =  "https://www.youtube.com/watch?v=eZC2Ohdk-wI"
    st.write('These ones are among the biggest hits: [Titanium(ft. SIA)](%s)' % url1, ', [Memories(ft. Kid Cudi)](%s)' % url2)

if option == 'Rock':
    Kyo = st.button('Kyo')
    Superbus = st.button('Superbus')
if option == 'Rock' and Superbus:
    url = "https://www.youtube.com/watch?v=CQPNj38WscM"
    st.write('Try this: [Butterfly](%s)' % url)
if option == 'Rock' and Kyo:
    url = "https://www.youtube.com/watch?v=hWXYnW2Um68"
    st.write('This song was a hit: [Le Graal](%s)' % url)
