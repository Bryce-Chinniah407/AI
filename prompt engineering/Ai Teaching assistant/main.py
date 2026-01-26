import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

def generate_response(prompt, temperature=0.3):
    try:
        response=client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=temperature
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"
    
def setup_ui():
    st.title("\n=== AI TEACHING ASSISTAN ===\n")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")

    user_input = st.text_input("Enter your question here:")

    if user_input:
        st.write(f"**Your question:** {user_input}")

        response = generate_response(user_input)

        st.write(f"**AI's answer:** {response}")
    else:
        st.write("Please enter a question to ask.")

def main():
    setup_ui()

if __name__ == "__main__":
    main()