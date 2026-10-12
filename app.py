
import streamlit as st
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key=PLACEHOLDER)

# Model
model = genai.GenerativeModel("models/gemini-3.8-flash")

# Page setup
st.set_page_config(
    page_title="Accessibility Assistant",
    page_icon="💡",
    layout="centered"
)

# Header
st.title("💡 Accessibility Assistant")

st.write(
    "Ask a question about supporting differently abled colleagues using Microsoft accessibility features."
)

st.divider()

# Example questions
st.write("### Try a question")

example_questions = [
    "How do I set up a screen reader?",
    "How can I increase the text size in Windows?",
    "How do I enable high contrast mode?"
]

for example in example_questions:
    if st.button(example):
        st.session_state["question"] = example

# Question input
question = st.text_input(
    "Your question",
    value=st.session_state.get("question", ""),
    placeholder="e.g. How do I set up a screen reader?"
)

# Ask button
if st.button("Ask Assistant", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching..."):

            prompt = f"""
You are an Accessibility Assistant.

Help IT technicians support differently abled colleagues using Microsoft accessibility features.

Question:
{question}
"""

            response = model.generate_content(prompt)

            st.success("Answer")
            st.write(response.text)