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
    st.session_state.pop("singular_input", None)
    st.session_state.pop("plural_input", None)
    st.rerun()


def select_vocabulary_areas() -> list[VocabularyAreas]:
    selected_areas = st.multiselect(
        "",
        options=[voc.value for voc in VocabularyAreas],
        placeholder="مَجَالاَتُ المُفْرَدَاتِ",
        label_visibility="collapsed",
    )

    if "areas_selected" not in st.session_state:
        st.session_state.areas_selected = False
    if "selected_enums" not in st.session_state:
        st.session_state.selected_enums = []

    if st.button("!أُمَارِسْ"):
        st.session_state.areas_selected = True
        st.session_state.selected_enums = [
            VocabularyAreas(label) for label in selected_areas
        ]

    if not st.session_state.areas_selected:
        st.stop()

    return st.session_state.selected_enums


def load_words(selected_enums: list[VocabularyAreas]):
    if "words" not in st.session_state:
        words: dict[str, Any] = {}
        for area in selected_enums:
            path = WORD_FACTORY[area]

            with open(path, "r", encoding="utf-8") as f:
                data: dict[str, Any] = json.load(f)
                words.update(data)

        st.session_state.words = words

    print(sorted(st.session_state.words.items()))
    with st.popover("اِفْتَحْ قَائِمَةَ الْكَلِمَاتِ"):
        for word, translation in sorted(st.session_state.words.items()):
            st.write(
                f"{word.capitalize()}:    {translation[0]}    -    {translation[1]}"
            )


def set_session_state():
    if "current_word" not in st.session_state or st.session_state.current_word == "":
        if not st.session_state.words:
            st.warning("No words left to practice")
            st.stop()
        st.session_state.current_word = random.choice(
            list(st.session_state.words.keys())
        )
        st.session_state.singular = st.session_state.words[
            st.session_state.current_word
        ][0]
        st.session_state.plural = st.session_state.words[st.session_state.current_word][
            1
        ]
        st.session_state.singular_stage = True
        st.session_state.plural_stage = False

    st.markdown(
        f"<div style='text-align: center; font-weight: bold; font-size: 2em;'> {st.session_state.current_word.upper()} </div>",
        unsafe_allow_html=True,
    )

    if st.button("❌ لا تُظْهِرِ الْكَلِمَةَ مَرَّةً أُخْرَى"):
        del st.session_state.words[st.session_state.current_word]
        rerun()


def singular_stage():
    st.text_input(
        label="Singular",
        placeholder="مُفْرَدٌ",
        key="singular_input",
        label_visibility="collapsed",
        value="",
    )
    if st.button("تَلْغِيزٌ", key="hint_singular"):
        st.error(st.session_state.singular)

    if st.session_state.singular_input:
        if validate_words(st.session_state.singular_input, st.session_state.singular):
            play_text(st.session_state.singular)
            st.markdown(
                f"<div style='text-align: center; font-weight: bold; font-size: 2em;'>  ✅ {st.session_state.singular.upper()}</div>",
                unsafe_allow_html=True,
            )
            st.session_state.plural_stage = True


def plural_stage():
    st.text_input(
        label="Plural",
        placeholder="جَمْعٌ",
        key="plural_input",
        label_visibility="collapsed",
    )
    if st.button("Hint", key="hint_plural"):
        st.error(st.session_state.plural)

    if st.session_state.plural_input:
        if validate_words(st.session_state.plural_input, st.session_state.plural):
            st.markdown(
                f"<div style='text-align: center; font-weight: bold; font-size: 2em;'>  ✅ {st.session_state.plural.upper()}</div>",
                unsafe_allow_html=True,
            )
            play_text(st.session_state.plural)
            if st.button("Siguiente palabra"):
                rerun()


def main():
    initialize()
    selected_enums = select_vocabulary_areas()
    load_words(selected_enums)
    set_session_state()

    # Example words dictionary

    if st.session_state.singular_stage:
        singular_stage()

    if st.session_state.plural is None:
        rerun()

    if st.session_state.plural_stage:
        plural_stage()


if __name__ == "__main__":
    main()
