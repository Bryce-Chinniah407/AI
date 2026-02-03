import streamlit as st
from openai import OpenAI
from PIL import Image
from io import BytesIO
import re
import io
import base64

client = OpenAI(api_key="")

def generate_response(prompt, temperature=0.3):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def run_ai_teaching_assistant():
    st.title("=== AI TEACHING ASSISTANT ===")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []

    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button("🧹 Clear Conversion", key="clear_ata"):
            st.session_state.history_ata = []

    with col_export:
        if st.session_state.history_ata:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_ata, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="Export Chat History",
                data=bio,
                filename="AI_Teaching_Assistant_Convertion.txt",
                mime="text/plain",
            )

    user_input = st.text_input("Enter your question here:", key="input_ata")

    if st.button("Ask", key="ask_ata"):
        if user_input.strip():
            with st.spinner("Generating AI response..."):
                response = generate_response(user_input.strip(), temperature=0.3)
            st.session_state.history_ata.append({"question": user_input.strip(), "answer": response})
            st.rerun()
        else:
            st.warning("⚠️Please enter a question before clicking Ask")

    st.markdown("### Conversion History")
    for idx, qa in enumerate(st.session_state.history_ata, start=1):
        st.markdown(f"**Q{idx}:** {qa['question']}")
        st.markdown(f"**A{idx}:** {qa['answer']}")

def main():
    st.sidebar.title("Choose AI Feature")
    option = st.sidebar.selectbox("", [
        "AI Teaching Assistant",
        "Math Mastermind",
        "Safe AI Image Generator"
    ])

    if option == "AI Teaching Assistant":
        run_ai_teaching_assistant()

if __name__ == "__main__":
    main()