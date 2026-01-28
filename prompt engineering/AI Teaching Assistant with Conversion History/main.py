import streamlit as st
from openai import OpenAI
import io

client = OpenAI(api_key="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")

def generate_response(prompt: str, temperature: float = 0.3) -> str:
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=temperature
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"
    
def setup_ui():
    st.set_page_config(page_title="AI TEACHING ASSISTANT", layout="centered")
    st.title("=== AI TEACHING ASSISTANT ===")
    st.write("Ask me anything about anything")

    if "history" not in st.session_state:
        st.session_state.history = []

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("🧹 Clear Conversation"):
            st.session_state.history = []
            st.experimental_rerun()

    with col_export:
        if st.session_state.history:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="Export Chat History",
                data=bio,
                file_name="AI_TEACHING_ASSISTANT_CONVERSION.txt",
                mime="text/plain",
            )

    user_input = st.text_input("Enter your question here: ")

    if st.button("Ask"):
        if user_input.strip():
            with st.spinner("Generate AI response..."):
                response = generate_response(user_input.strip())
            st.session_state.history.append(
                {"question": user_input.strip(), "answer": response}
            )
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")

    st.markdown("### Conversion History")
    st.markdown(
        """
    <style>
    .history-box {
        max-height: 400px;
        overflow-y: auto;
        border: 1px solid #ddd;
        padding: 12px;
        background-color: #f9f9f9;
        border-raius: 6px;
        font-family: 'Seguo UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .question {
        font-weight: 600;
        color: #0a6ebd;
        margin-top: 12px;
        margin-bottom:m 4px;
        
    }"""
    )