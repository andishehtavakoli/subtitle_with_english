import streamlit as st
from src.pars_subtitle import Subtitle
from src.data import DATA_DIR
from src.utils.io import read_json, write_json

st.header(':clapper: Learn English with Movie')
uploaded_file = st.file_uploader('Upload a subtitle(.srt format):' , type=['srt'])
# TODO : Write uploaded file in a temporary location

file_path = DATA_DIR /'Game of Thrones _Winter is Coming_en.srt'
s = Subtitle(file_path)
user_level = st.slider('Enter your English Level(0:Elementaray, 10:Advance)', min_value=0, max_value=10)

# read tracker
tracker = read_json(DATA_DIR / 'tracker.json')

# read subtitle
st.subheader('Vocabulary')
cols = st.columns(2)
if cols[0].button('Previous'):
    tracker['sub_position'] -= 1

if cols[1].button('Next'):
    tracker['sub_position'] += 1



st.write(s.subtitle[tracker['sub_position']].text)

# write tracker
tracker = write_json(tracker, DATA_DIR / 'tracker.json')


