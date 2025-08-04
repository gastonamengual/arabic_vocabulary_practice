import io
import unicodedata

import streamlit as st
from gtts import gTTS


def play_text(text: str):
    tts = gTTS(text=text, tld="com.eg", lang="ar")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format="audio/mpeg")


def validate_words(word1: str, word2: str) -> bool:
    return unicodedata.normalize("NFC", word1) == unicodedata.normalize("NFC", word2)


def initialize() -> None:

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
