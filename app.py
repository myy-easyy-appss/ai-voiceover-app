import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(page_title="AI Voiceover Generator", page_icon="🎙️")

st.title("🎙️ AI Voiceover Generator")
st.write("Type your text and instantly generate a realistic AI voice!")

# Input text
text = st.text_area("Enter your text below:", height=150)

# Select voice
voices = ["en-US-GuyNeural", "en-US-JennyNeural", "en-GB-RyanNeural", "en-IN-NeerjaNeural"]
voice = st.selectbox("Choose a voice:", voices)

# File name
file_name = "output.mp3"

async def tts(text, voice):
    if text.strip() == "":
        st.warning("Please enter some text!")
        return
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_name)
    st.success("✅ Voice generated successfully!")
    audio_file = open(file_name, "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Button to trigger
if st.button("Generate Voice 🎧"):
    asyncio.run(tts(text, voice))
