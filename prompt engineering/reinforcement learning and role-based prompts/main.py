import openai

client = openai.OpenAI(api_key="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")

def generate_response(prompt, temperature=0.3):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def reinforcement_learning():
    print("\n=== REINFORCEMENT LEARNING ===\n")

    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}")

    rating = int(input("\nRate the response from 1 (bad) to 5 (good: )"))
    feedback = input("Provide Feedback >  ")

    improved_response = (
        f"{initial_response}\n\n"
        f"🔁 Improve using your feedback:\n{feedback}"
    )

    print(f"\nImproved ai response using feedback:\n{improved_response}")

def role_based_prompt():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")

    category = input(f"Enter a category (e.g., science, history, maths):")
    item = input(f"Enter a specific {category} topic: ")

    teacher_prompt = f"You are a teacher. Explain {item} from {category} in simple terms"

    expert_prompt = f"You are a/an {category} expert. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt)
    expert_response = generate_response(expert_prompt)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n\n\n\n--- Expert's Perspective ---\n{expert_response}")

def run_activity():
    print("\n=== AI Learning Activity ===")

    choice = input("Which activity would you like to run?\n"
                   "1/: Reinforcement learning\n"
                   "2/: Role-Based Prompts\n"
                   "Enter choice:"
                   )
    
    if choice == "1":
        reinforcement_learning()
    elif choice == "2":
        role_based_prompt()

    else:
        print("❌ Invalid choice.")

if __name__ == "__main":
    run_activity()