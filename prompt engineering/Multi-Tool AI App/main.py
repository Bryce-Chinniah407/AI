import streamlit as st
from openai import OpenAI
from PIL import Image
from io import BytesIO
import re
import io
import base64

client = OpenAI(api_key="")

def generate_maths_response(prompt, temperature):
    system_prompt = """You are a Maths Mastermind. Solve problems with step by step explanation"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

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
    
def run_math_mastermind():
    st.title("Maths Mastermind")
    st.write("**Your Expert Mathematical Problem Solver**")

    if "history_mm" not in st.session_state:
        st.session_state.history_mm = []
    if "input_key_mm" not in st.session_state:
        st.session_state.input_key_mm = 0

    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button(" 🧹 Clear Conversion", key="clear_mm"):
            st.session_state.history_mm = []
            st.rerun()

    with col_export:
        if st.session_state.history_mm:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_mm, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="Export Math Solutions",
                data=bio,
                file_name="Math_Mastermind_Solution.txt",
                mime="text/plain",
            )

    with st.form(key="math_form", clear_on_submit=True):
        user_input = st.text_area(
            "Enter your math problem here:",
            height=100,
            placeholder="Example: Solve x^2 + 5x 6 = 0",
            key=f"user_input_{st.session_state.input_key_mm}"
            )   

        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button("Solve Problem", use_container_width=True)
        with col2:
            difficulty = st.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

        if submitted and user_input.strip():
            enhanced_prompt = f"[{difficulty} Level] {user_input.strip()}"
            with st.spinner("Solving your math problem..."):
                response = generate_maths_response(enhanced_prompt)
            st.session_state.history_mm.insert(0, {
                "question": user_input.strip(),
                "answer": response,
                "difficulty": difficulty
            })
            st.session_state.input_key_mm += 1
            st.rerun()
        elif submitted and not user_input.strip():
            st.warning("⚠️ Please enter a maths problem.")

    if st.session_state.history_mm:
        st.markdown("### Solution History")
        for idx, qa in  enumerate(st.session_state.history_mm):
            question_num = len(st.session_state.history_mm) - idx
            difficulty_badge = f"[{qa.get('difficulty', 'N/A')}]"
            st.markdown(f"**Problem {question_num} {difficulty_badge}:** {qa['question']}")
            st.markdown(f"**Solution {question_num}: *\n{qa['answer']}")

        
def run_ai_safe_image_generator():
    st.title("Safe AI Image Generator")
    st.write("Generate image using OpenAI Safely.")

    def is_prompt_safe(prompt: str) -> bool:
        forbidden_keywords = [
            "violence", "weapon", "gun", "blod", "nude", "porn"
, "drugs", "hate", "sex", "terror"]
        pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)
        return not bool(pattern.search(prompt))        


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
    elif option == "Math Mastermind":
        run_math_mastermind()
    elif option == "Safe AI Image Generator":
        run_ai_safe_image_generator()

if __name__ == "__main__":
    main()