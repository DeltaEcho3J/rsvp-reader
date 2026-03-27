
import streamlit as st
import time

def highlight_middle(word, width = 20):
    mid = len(word) // 2

    padded = word.center(width)

    mid = len(padded)//2
    return (
        padded[:mid]
        + f"<span style='color:red'>{padded[mid]}</span>"
        + padded[mid+1:]
    )

inp_text = st.text_area("Enter text:")

if inp_text:
    words = inp_text.split()
    placeholder = st.empty()
    speed_wpm = st.slider("Select your reading WPM", min_value=100, max_value=900, value=25)

    delay = 60/speed_wpm
    if st.button("Start"):
        for word in words:
            styled_word = highlight_middle(word)

            placeholder.markdown(
                f"""
                <div style='
                    text-align:center;
                    font-family: monospace;
                    font-size: 48px;
                    width: 100%;
                '>
                    {styled_word}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(delay)
