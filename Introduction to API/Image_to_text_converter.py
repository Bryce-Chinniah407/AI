import requests
from PIL import Image
import io
import os
from colorama import init, Fore, Style
import json

init(autoreset=True)

def query_hf_api(api_url, payload):
    headers = {"Authorization": f"Bearer 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"}
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"status {response.status_code}: {response.text}")
    return response.json

def get_basic_caption(image, model="nlpconnect/vit-gpt2-image-captioning"):
    print(f"{Fore.YELLOW}Generating basic caption... ")

    api_url = f"https://router.huggingface.co/models/{model}"

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)

    headers = {"Authorization": f"Bearer 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"}
    response = requests.post(api_url, headers=headers, data=buffered.getvalue())

    if response.status_code != 200:
        return f"[Error] {response.status_code}: {response.text}"
    
    result = response.json()

    if isinstance(result, dict) and "error" in result:
        return result[0].get("generated_text", "No cation generated.")
    
def generate_text(prompt, model="gpt2", max_new_tokens=60):
    print(f"{Fore.CYAN}Generating text... ")

    api_url = f"https://router.huggingface.co/models/{model}"
    payload = {
        "inputs":prompt,
        "parameters": {"max_new_tokens": max_new_tokens}
    }

    result = query_hf_api(api_url, payload)

    if isinstance(result, dict) and "error" in result:
        raise Exception(result["error"])
    
    return result[0].get("generated_text", "")

def truncate_text(text, word_limit):
    words = text.strip().split()
    return " ".join(words[:word_limit])

def print_menu():
    print(f"""{Style.BRIGHT}
          
{Fore.GREEN}=================Image-to-Text Conversion =================
1. Caption (5 words)
2. description (30 words)
3. Summary (50 words)
4. Exit
===================================================================
""")
    
def main():
    image_path = input(f"{Fore.BLUE}Enter image path: ")

    if not os.path.exists(image_path):
        print(f"{Fore.RED}Failed to open image: {e}")
        return
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}Failed to open image: {e}")
        return
    basic_caption = get_basic_caption(image)
    print(f"{Fore.YELLOW}Basic caption: {Style.DIM}{basic_caption}\n")

    while True:
        print_menu()
        choice = input(f"{Fore.CYAN}Enter choice (1-4): ")

        if choice == "1":
            print(f"{Fore.GREEN}Caption: {truncate_text(basic_caption, 5)}\m\n")
        
        elif choice == "2":
            prompt = f"Expand this caption into exactly 30 words:   {basic_caption}"
            try:
                text = generate_text(prompt, max_new_tokens=40)
                print(f"{Fore.GREEN}Description: {truncate_text(text, 30)}")
            except Exception as e:
                print()