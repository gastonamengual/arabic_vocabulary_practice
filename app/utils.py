import base64
import io
import unicodedata

import streamlit as st
from gtts import gTTS

IMAGE_FILE = "app/alhambra.jpg"
OVERLAY_OPACITY = 0.5


def play_text(text: str):
    tts = gTTS(text=text, tld="com.eg", lang="ar")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format="audio/mpeg")


def validate_words(word1: str, word2: str) -> bool:
    return unicodedata.normalize("NFC", word1) == unicodedata.normalize("NFC", word2)


@st.cache_resource
def get_base64_of_bin_file(bin_file: str):
    print(bin_file)
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def initialize():
    st.markdown(
        """
        <style>
        textarea {
            font-size: 1.4rem !important;
        }
        input {
            font-size: 1.4rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    bin_str = get_base64_of_bin_file(IMAGE_FILE)
    css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, {OVERLAY_OPACITY}), rgba(0, 0, 0, {OVERLAY_OPACITY})),
                    url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    input[type="text"] {{
        text-align: center;
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    st.markdown(
        "<div style='text-align: center; font-weight: bold; font-size: 3em;'>☪️ مُـمَارَسَةٌ العَرَبِيَّةِ 🕌</div>",
        unsafe_allow_html=True,
    )
