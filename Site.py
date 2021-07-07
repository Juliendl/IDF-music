import streamlit as st
import pandas as pd
import numpy as np

st.title('''
   Welcome to the first music recommendation !      
''')

# input = ['Bal musette', 'Jazz', 'Punk', 'Rock', 'Rap',
#          'RnB', 'Dancehall/Ragga', 'Reggaeton', 'Zouglou',
#          'Coupé-décalé', 'Logoby', 'Zouk', 'Disco', 'French Touch',
#          'Turntablism/platinisme', 'Tecktonik', 'Electro', 'Folk',
#          'Jazz', 'Pop rock', 'Reggae', 'Country', 'Blues',
#          'Rock garage', 'World', 'Ska', 'Raï', 'Gypsy pop', 'Tango', 'Opérette', 'Variété']
input = ['Rap', 'Electro', 'Rock', ]

dic = {
    'in': input,
    'out': {
        'Rock': 'Louise attaque, Superbus, Kyo',
        'Rap': 'Booba, Nekfeu',
        'Electro': 'David Guetta',
        'Variété': 'Vianney, Kendji Girac, GIMS'

    }
}

# user_input = st.text_input("50/50. Gimme a song", "Artist - Title")

option = st.selectbox(
    'Tell me more about you. What is your style of music?',
    dic['in'])

st.cache()
out = dic['out'][option]
'Check for this: ', out
st.write('Want to learn more about these?')
artistes = st.button(out)
if artistes:
    st.write('The biggest hit is Titanium(ft Sia)')
