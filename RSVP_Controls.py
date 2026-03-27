
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

def highlight_paragraph(words, current_index):
    styled_words = []

    for i, word in enumerate(words):
        if i ==current_index:
            styled_words.append(f"<span style='color:red'>{word}</span>")
        else:
            styled_words.append(word)
    return " ".join(styled_words)
inp_text = st.text_area("Enter text:")

if inp_text:
    words = inp_text.split()
    placeholder = st.empty()
    paragraph_placeholder = st.empty()
    speed_wpm = st.slider("Select your reading WPM", min_value=100, max_value=900, value=25)

    delay = 60/speed_wpm
    if st.button("Start"):
        for i, word in enumerate(words):
            # RSVP display
            styled_word = highlight_middle(word)

            placeholder.markdown(
                f"""
                <div style='
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    height:200px;
                    font-family: monospace;
                    font-size: 48px;
                '>
                    <div style='width: 20ch; text-align: center;'>
                        {styled_word}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Paragraph display
            paragraph_html = highlight_paragraph(words, i)

            paragraph_placeholder.markdown(
                f"""
                <div style='
                    margin-top: 30px;
                    font-size: 20px;
                    line-height: 1.6;
                    text-align: center;
                    max-width: 800px;
                    margin-left: auto;
                    margin-right: auto;
                '>
                    {paragraph_html}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(delay)

            

