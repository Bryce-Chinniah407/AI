import os
from openai import OpenAI

API_KEY = "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"

client = OpenAI(api_key=API_KEY)

def generate_response(prompt, temperature=0.3):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )

        return  response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def run_activity():
    print("\n=== ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY ===\n")

    category = input("Enter a category (e.g., animal, food, city): ")
    item = input(f"Enter a specific {category} to classify: ")

    print("\n--- ZERO-SHOT LEARNING ---")
    zero_shot = f"Is {item} a {category}? Answer yes or no."
    print(f"Prompt: {zero_shot}")
    print(f"Response: {generate_response(zero_shot)}")

    print("\n--- ONE-SHOT LEARNING ---")
    one_shot = f"""Determine if the item belongs to the category.
Example:
Category: fruit
item: apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print(f"Response: {generate_response(one_shot)}")

    print("\n--- FEW-SHOT LEARNING ---")
    few_shot = f"""Determine if the item belongs to the category.
Example1:
Category: fruit
item: apple
Answer: Yes, apple is a fruit.

Example2:
Category: car
item: banana
Answer: No, banana is not a car. It's a fruit.

Example3:
Category: weather types
item: rain
Answer: yes, rain is a weather type.

Now you try:
Category: {category}
Item: {item}
Answer: """
    print(f"Response: {generate_response(few_shot)}")

    print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
    creative_prompt = f"""Write a one-sentence story about the given word.

Example1:
Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Example2:
Word: computer
Story: The computer sighed as another cup of coffeewas spilled on its keyboard.

Word: {item}
Story: """
    
    print(f"Response: {generate_response(creative_prompt, temperature=0.7)}")
    

if __name__ == "__main__":
    run_activity()










