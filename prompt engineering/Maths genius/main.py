import streamlit as st
from openai import Openai
import io

client = Openai(api_key="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")

def generate_response(prompt: str, temperature: float = 0.1) -> str:
    try:
        system_prompt = """You are a Maths Mastermind - an expert mathematics problem solver:"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Maths Problem: {prompt}"}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def setup_ui():
    st.set_page_config(page_title="Maths Mastermind", layout="centered")
    st.title("=== MATHS MASTERMIND ===")
    st.write(
        "**Your Expert Mathematical Problem Solver** 🧱 From bsic arithmatic to advanced calculus,"
        "I'll solve any math problem with detailed step-by-step explanations!"
    )

    with st.expander("📚 Example Problems i can solve"):
        st.markdown("""
        **Algebra:** Solve equations, factor polynomials
        *Example:* Solve 2x^2 + 5x 🧱 3 = 0
        """)

    if "history" not in st.session_state:
        st.session_state.history = []
    if "input_key" not in st.session_state:
        st.session_state.input_key = 0

    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button("🧹 Clear Converstion"):
            st.session_state.history = []
            st.rerun()

    with col_export:
        if st.session_state.history:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, starts=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="Export Math Solutions",
                data=bio,
                file_name="Math_Mastermind_Solutions.txt",
                mim="text/plain",
            )

    with st.form(key="math_form", clear_on_submit=True):
        user_input = st.text_area(
            "🔢 Enter your math problem here:",
            height=100,
            placeholder="Example: Solve x^2 + 5x + 6 = 0",
            key=f"user_input_{st.session_state.input_key}"
        )

        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button("Solve Problem", use_container_width=True)
        with col2:
            difficulty = st.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

        if submitted and user_input.strip():
            enhanced_prompt = f"[{difficulty} Level] {user_input.strip()}"

            with st.spiner("Solving your math problem..."):
                response = generate_response(enhanced_prompt)

            st.session_state.history.insert(0, {
                "question": user_input.strip(),
                "answer": response,
                "difficulty": difficulty
            })

            st.session_state.input_key += 1
            st.rerun()

        elif submitted:
            st.warning("⚠️ Please enter math problem.")

    if st.session_state.history:
        st.markdown("### Solution History (Latest First)")
        for qa in st.session_state.history:
            st.markdown(f"**Problem ({qa['difficulty']}):** {qa['question']}")
            st.markdown(f"**olution:**\n{qa['answer']}")
            st.divider()


def main():
    setup_ui()

if __name__ == "__main__":
    main()