from openai import OpenAI
from colorama import init, Fore, Style

init(autoreset=True)

client = OpenAI(api_key="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")

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
    
def get_essay_details():
    print(Fore.CYAN + "\n=== AI Writing Assistant ===\n")

    topic = input(Fore.YELLOW + "Enter the topic of your essay: ")
    essay_type = input(Fore.YELLOW + "What type of essay are you writing? (Arguementative, Narrative, Descriptive, Analytical, Persuasive): ")

    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print(Fore.GREEN + "1. 300 words")
    print(Fore.GREEN + "2. 900 words")
    print(Fore.GREEN + "3. 1200 words")
    print(Fore.GREEN + "4. 2000 words")

    word_count_choice = input(Fore.YELLOW + "Enter choice number: ")
    word_count_dict = {"1": "300", "2": "900", "3": "1200", "4": "2000"}
    length = word_count_dict.get(word_count_dict, "300")

    target_audience = input(Fore.YELLOW + "Target Audience: ")
    specific_points = input(Fore.YELLOW + "Specific points included: ")

    stance = input(Fore.YELLOW + "Your stance (For / Against / Neutral): ")
    references = input("Any source or references?: ")
    writing_style = input(Fore.YELLOW + "Prefered writing style (Formal, Academic, Creative): ")

    outline_needed = input(Fore.YELLOW + "Would you like an outline? (Yes/No): ").lower()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience,
        "specific points": specific_points,
        "stance": stance,
        "references": references,
        "writing_style": writing_style,
        "outline_needed": outline_needed,
    }

def generate_essay(details):
    temperature = float(input(Fore.YELLOW + "Enter temperature (0.2 = structured, 0.7 = creative): "))

    introduction_prompt = (
        f"Write an introduction for a {details['essay_type']} essay"
        f"on '{details['topic']}' with a {details['stance']} stance."
    )

    introduction = generate_response(i)