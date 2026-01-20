from openai import OpenAI

client = OpenAI(api_key="")

def generate_response(prompt, temperature=0.3):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=temperature
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"
    
def bias_mitigation():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")

    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}")

    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a good doctor'):")
    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI Response (Neutral):\n{modified_response}")

def token_limit():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")

    long_prompt = input("Enter a long prompt (more than 300 words): ")
    long_response = generate_response(long_prompt)
    print(f"\nResponse to Long Prompt:\n{long_response[:500]}...")

    short_prompt = input("Now, condense the prompt to be more concise: ")
    short_response = generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt:\n{short_response}")

def main():
    print("\n=== AI Learning Activity ===")

    activity_choice = input("Which activity would you like to run? (1: Bias Mitigation, 2: Token Limits): ")

    if activity_choice == "1":
        bias_mitigation()
    elif activity_choice == "2":
        token_limit()
    else:
        print("Invalid choice. Please choose either 1 or 2.")

if __name__ == '__main__':
    main()