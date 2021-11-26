import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(page_title = 'Happy Birthday', layout = 'wide', page_icon='🤡')

# st.balloons()

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
  "hearts": "https://assets8.lottiefiles.com/packages/lf20_mz70xctt.json"
}

st.title("Гузя, с днем рождения!")
st.title("🎉🎉🎉 🥳🥳🥳 🎈🎈🎈")
st.balloons()
st.subheader('Включай песню...')

audio_file = open('House of Pain - Jump Around.mp3', 'rb')
audio_bytes = audio_file.read()

Song = st.audio(audio_bytes, format='audio/mp3')
st.subheader('Считай до 10...')
st.subheader('Жми кнопку 👇')
Button = st.button('🎁 ЖМИ 🎁')

if not Button:
    st.stop()
else:
    st.header('👇👇👇')
    st.balloons()
    c1,c2,c3,c4 = st.columns(4)
    with c1:
      st_lottie(load_lottieurl(links["bot"]),key="1")
      st_lottie(load_lottieurl(links["DS"]),key="5")
      st.title("Желаю ярких эмоушенс...")
    with c2:
      st_lottie(load_lottieurl(links["face"]),key="3")
      st_lottie(load_lottieurl(links["bot-DS"]),key="4")
      st.title("искренних филингс ...")
    with c3:
      st_lottie(load_lottieurl(links["process"]),key="2")
      st_lottie(load_lottieurl(links["net"]),key="7")
      st.title("и большой лав 👉💍👰🤍🤵")
    with c4:
      st_lottie(load_lottieurl(links["love"]),key="6")
      st_lottie(load_lottieurl(links["hearts"]),key="11")
      st.title("🎉🎉🎉 🥳🥳🥳 🎈🎈🎈🍰🍰🍰")
      st_lottie(load_lottieurl(links["dash"]),key="10")
      st.write("*with love from Nick 😈😈😈")
      # st_lottie(load_lottieurl(links["DS"]),key="9")
