from openai import OpenAI

OPENAI_API_KEY = "API_KEY"

try:
    client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    print("❌ Failed to initialize OpenAI client: ", e)
    exit()

def generate_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
    
def silly_prompt():
    print("\nAI Prompt Engineering Tutorial")
    print("-----------------------------")
    print("Concepts Covered: ")
    print("> Clarity & Specificity")
    print("> Contextual Information")

    print("\n🟡 STEP 1: Enter a vague prompt")
    vague_prompt = input("> ")
    print("\n🤖 AI Response (Vague Prompt):")
    print("-" * 40)
    print(generate_response(vague_prompt))

    print("\n🟢 STEP 2: Make the prompt MORE SPECIFIC")
    specific_prompt = input("> ")
    print("🤖 AI Response (Specific Prompt):")
    print("-" * 40)
    print(generate_response(specific_prompt))

    print("\n🔵 STEP 3: Add CONTEXT to the question")
    very_specific_prompt = input("> ")
    print("🤖 AI Response (contextual Prompt):")
    print("-" * 40)
    print(generate_response(very_specific_prompt))


if __name__ == "__main__":
    silly_prompt()