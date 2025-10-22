import streamlit as st
import edge_tts
import asyncio
import os

st.title("🎙️ Voiceover Generator")

# Initialize
if "text_blocks" not in st.session_state:
    st.session_state.text_blocks = ["Welcome to my app!", "This is a demo.", "Enjoy your day!"]

# Add new text input
new_text = st.text_input("Add a new line:")
if st.button("Add"):
    if new_text:
        st.session_state.text_blocks.append(new_text)
        st.success("Added successfully!")

# Reorder section
st.subheader("Reorder lines 🧩")
positions = []
for i, text in enumerate(st.session_state.text_blocks):
    pos = st.number_input(f"Position for line {i+1}: {text}", min_value=1, max_value=len(st.session_state.text_blocks), value=i+1)
    positions.append((text, pos))

if st.button("Apply Order"):
    st.session_state.text_blocks = [t for t, _ in sorted(positions, key=lambda x: x[1])]
    st.success("Reordered successfully!")

st.write("### Final Order:")
for line in st.session_state.text_blocks:
    st.write(f"- {line}")

# Generate audio
voice = st.selectbox("Choose Voice:", ["en-US-AriaNeural", "en-GB-RyanNeural"])
if st.button("Generate Voice"):
    async def generate_audio():
        communicate = edge_tts.Communicate(" ".join(st.session_state.text_blocks), voice)
        await communicate.save("output.mp3")
        st.audio("output.mp3")

    asyncio.run(generate_audio())
