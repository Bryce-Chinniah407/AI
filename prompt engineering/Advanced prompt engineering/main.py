import os
import time
from google import genai
from google.genai import types

import time

GEMINI_API_KEY = "AIzaSyCbQm5xHdMhzs1V3nMk_ZyOJA3ZLv4FVBs"

def generate_response(prompt, temperature=0.5):
    model_id = "gemini-2.0-flash"

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        time.sleep(2)

        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
            ),
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "Error: Rate limit exceeded. Please wait 10 seconds and try again."
        return f"Error: {str(e)}"
    
def temperature_prompt_activity():
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)
    print("\nIn this activity we'll explore:")
    print("1. How temperature affects AI creativity and randomness")
    print("2. How instruction-based prompts can control AI outputs")

    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    base_prompt = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint'):   ")

    print("\nGenerating response with different temperature settings...")
    print("\n--- LOW TEMPERATURE (0.1) - MORE DETERMINISTIC ---")
    low_temp_response = generate_response(base_prompt, temperature=0.1)
    print(low_temp_response)

    time.sleep(1)
    print("\n--- MEDIUM TEMPERATURE (0.5) - Balanced ---")
    medium_temp_response = generate_response(base_prompt, temperature=0.5)
    print(medium_temp_response)

    time.sleep(1)

    print("\n--- HIGH TEMPERATURE (0.9) - MORE Random/Creative ---")
    high_temp_response = generate_response(base_prompt, temperature=0.9)
    print(high_temp_response)

if __name__ == "__main__":
    temperature_prompt_activity()