import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="AI Voiceover Generator", page_icon="🎙️")

st.title("🎙️ AI Voiceover Generator")
st.write("Type your text and instantly generate a realistic AI voice!")

# Input text
text = st.text_area("Enter your text below:", height=150)

# Select accent
accent = st.selectbox("Select accent:", ["US", "UK", "India", "Australia", "Canada"])
voice_dict = {
    "US": "en",
    "UK": "en-uk",
    "India": "en-in",
    "Australia": "en-au",
    "Canada": "en-ca"
}
lang_code = voice_dict[accent]

# File name
file_name = "output.mp3"

# Generate voice
if st.button("Generate Voice 🎧"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            tts = gTTS(text=text, lang=lang_code)
            tts.save(file_name)
            st.success("✅ Voice generated successfully!")
            st.audio(file_name, format="audio/mp3")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
