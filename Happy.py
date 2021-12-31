import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(page_title = 'Happy New Year', page_icon='🎅🏻')


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


links={
  "bot":"https://assets7.lottiefiles.com/packages/lf20_zh0yCH.json",
  "face" : "https://assets3.lottiefiles.com/packages/lf20_fnjH1K.json",
  "process" : "https://assets3.lottiefiles.com/packages/lf20_LmfDtl.json",
  "DS" : "https://assets10.lottiefiles.com/packages/lf20_i6sqnxav.json",
  "net":"https://assets5.lottiefiles.com/private_files/lf30_smtnx4ug.json",
  "bot-DS":"https://assets10.lottiefiles.com/packages/lf20_6aYlBl.json",
  "dash":"https://assets2.lottiefiles.com/packages/lf20_d6YcaL.json",
  "chem":"https://assets3.lottiefiles.com/temp/lf20_IAVB8U.json",
  "singer": "https://assets4.lottiefiles.com/packages/lf20_H9cy3V.json",
  "love": "https://assets8.lottiefiles.com/private_files/lf30_5etnzhz4.json",
  "hearts": "https://assets8.lottiefiles.com/packages/lf20_mz70xctt.json",

  'year22': "https://assets9.lottiefiles.com/packages/lf20_fnefuebd.json",
  "santa": "https://assets9.lottiefiles.com/packages/lf20_7si4uwcv.json",
  "confetti":"https://assets9.lottiefiles.com/private_files/lf30_exa5jczj.json",
  "fireworks":"https://assets9.lottiefiles.com/packages/lf20_2pr9x3si.json",
  "button":"https://assets3.lottiefiles.com/datafiles/ft3xlpduRes83XO/data.json"
}

# st.title("Гузя, с днем рождения!")
# st.header("🎉🎉🎉 🥳🥳🥳 🎈🎈🎈")
st.balloons()
st.subheader('Включай песню...')

audio_file = open('House of Pain - Jump Around.mp3', 'rb')
audio_bytes = audio_file.read()

Song = st.audio(audio_bytes, format='audio/mp3')
st.subheader('Считай до 10...')
st.subheader('Жми кнопку 👇')
Button1 = st.button('🎅🏻 ЖМИ 🎅🏻')

if not Button1:
    st.stop()
else:
    st.balloons()
    st_lottie(load_lottieurl(links["confetti"]),key="0")
#     st.title("Желаю...")
    st_lottie(load_lottieurl(links["DS"]),key="5")
    st.title("Еще больше результатов")
    st_lottie(load_lottieurl(links["face"]),key="3")
    st_lottie(load_lottieurl(links["bot-DS"]),key="4")

    st.title("и ярких эмоций")
    st_lottie(load_lottieurl(links["fireworks"]),key="7")
    st_lottie(load_lottieurl(links["santa"]),key="2")
    
    st.title("В новом году ✨")
    st.title("🎉🎉🎉 🥳🥳🥳")
    st_lottie(load_lottieurl(links["year22"]),key="1")

    st.write("*made with love from Nick 😈😈😈")
