import json
import random
from typing import Any

import streamlit as st

from app.models import WORD_FACTORY, VocabularyAreas
from app.utils import initialize, play_text, validate_words


def rerun() -> None:
    st.session_state.current_word = ""
    st.session_state.singular_stage = True
    st.session_state.plural_stage = False
    if "singular_input" in st.session_state:
        del st.session_state["singular_input"]
    if "plural_input" in st.session_state:
        del st.session_state["plural_input"]
    st.rerun()


st.markdown(
    "<div style='text-align: center; font-weight: bold; font-size: 3em;'>☪️ تَدْرِيبُ المُفْرَدَاتِ العَرَبِيَّةِ 🕌</div>",
    unsafe_allow_html=True,
)
selected_areas = st.multiselect(
    "Select vocabulary areas:", options=[voc.value for voc in VocabularyAreas]
)
selected_enums = [VocabularyAreas(label) for label in selected_areas]

if not selected_enums:
    st.stop()

if "words" not in st.session_state:
    words: dict[str, Any] = {}
    for area in selected_enums:
        path = WORD_FACTORY[area]

        with open(path, "r", encoding="utf-8") as f:
            data: dict[str, Any] = json.load(f)
            words.update(data)

    st.session_state.words = words

initialize()

if "current_word" not in st.session_state or st.session_state.current_word == "":
    st.session_state.current_word = random.choice(list(st.session_state.words.keys()))
    st.session_state.singular = st.session_state.words[st.session_state.current_word][0]
    st.session_state.plural = st.session_state.words[st.session_state.current_word][1]
    st.session_state.singular_stage = True
    st.session_state.plural_stage = False

st.markdown(
    f"<div style='text-align: center; font-weight: bold; font-size: 2em;'> {st.session_state.current_word.upper()} </div>",
    unsafe_allow_html=True,
)
if st.button("❌"):
    del st.session_state.words[st.session_state.current_word]
    rerun()

if st.session_state.singular_stage:
    st.text_input(
        label="Singular",
        placeholder="مُفْرَدٌ",
        key="singular_input",
        label_visibility="collapsed",
    )

    if st.session_state.singular_input:
        if validate_words(st.session_state.singular_input, st.session_state.singular):
            play_text(st.session_state.singular)
            st.markdown(
                f"<div style='text-align: center; font-weight: bold; font-size: 2em;'>  ✅ {st.session_state.singular.upper()}</div>",
                unsafe_allow_html=True,
            )
            st.session_state.plural_stage = True
        else:
            st.warning(f"Hint: {st.session_state.singular}")

if st.session_state.plural is None:
    rerun()

if st.session_state.plural_stage:
    st.text_input(
        label="Plural",
        placeholder="جَمْعٌ",
        key="plural_input",
        label_visibility="collapsed",
    )
    if st.session_state.plural_input:
        if validate_words(st.session_state.plural_input, st.session_state.plural):
            st.markdown(
                f"<div style='text-align: center; font-weight: bold; font-size: 2em;'>  ✅ {st.session_state.plural.upper()}</div>",
                unsafe_allow_html=True,
            )
            play_text(st.session_state.plural)
            if st.button("Siguiente palabra"):
                rerun()
        else:
            st.warning(f"Hint: {st.session_state.plural}")
