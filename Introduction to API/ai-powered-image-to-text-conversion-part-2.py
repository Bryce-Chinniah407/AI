import requests
from PIL import Image
import io
import os
from colorama import init, Fore, Style

init(autoreset=True)

HF_HEADERS = {
    "Athorization": f"Bearer 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"
}

def hf_post(api_url, *, data=None, json_payload=None):
    response = requests.post(
        api_url,
        headers=HF_HEADERS,
        data=data,
        json=json_payload,
        timeout=60
    )

    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}: {response.text}")
    
    return response.json()

def get_basic_caption(image, model="nlpconnect/vit-gpt2-image-captioning"):
    print("Generating Image caption... ")

    api_url = f"https://router.huggingface.co/hf-inference/models/{model}"

    buffered = io.BytesIO()
    image.convert("RGB").save(buffered, format="JPEG")
    buffered.seek(0)

    try:
        result = hf_post(api_url, dat=buffered.read())
    except Exception as e:
        return f"API Error: {e}"
    
    if isinstance(result, dict) and "error" in result:
        return f"HF Error: {result['error']}"
    
    if not isinstance(result, list) or len(result) == 0:
        return "No caption generated"
    
    return result[0].get("generated_text", "No caption generated")

def generate_text(prompt, model="google/flan-t5-small", max_new_tokens=60):
    print("Generating text...")

    api_url = f"https://router.huggingface.co/hf-inference/models/{model}"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens
        }
    }

    result = hf_post(api_url, json_payload=payload)

    if isinstance(result, dict) and "error" in result:
        raise Exception(f"HF Error: {result['error']}")
    
    if not isinstance(result, list) or len(result) == 0:
        raise Exception("Empty response from model")
    
    return result[0]["generated_text"]

def truncate_text(text, word_limit):
    return " ".join(text.strip().split()[:word_limit])

def force_word_count(text, count):
    words = text.split()
    if not words:
        return""
    while len(words) < count:
        words.append(words[-1])
    return " ".join(words[:count])

def print_menu():
    print(f"""{Fore.GREEN}========= Image-to-Text =========\n1. Caption (5 words)\n2. Description (30 words)\n3. Summary    (50 words)\n4. Exit (0 words)\n===================================""")

def main():
    try:
        image_path = input(f"{Fore.BLUE}Enter image path: {Style.RESET_ALL}").strip()

        if not os.path.exists(image_path):
            print(f"{Fore.RED}File not found.")
            return
        
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"{Fore.REDE}Image open failed: {e}")
            return
        
        basic_caption = get_basic_caption(image)
        print(f"\n{Fore.YELLOW}Basic caption: {basic_caption}\n")

        while True:
            print_menu()
            choice = input(f"{Fore.CYAN}Choice (1-4): {Style.RESET_ALL}").strip()

            if choice == "1":
                print(force_word_count(basic_caption, 5))

            elif choice == "2":
                prompt = (
                    "Write a description of exactly 30 words. "
                    "Do not use more or fewer words."
                    f"Caption: {basic_caption}"
                )
                text = generate_text(prompt, max_new_tokens=50)
                print(force_word_count(text, 30))

            elif choice == "3":
                prompt = (
                    "Write a summary of exactly 50 words. "
                    "Do not use more or fewer words."
                    f"Caption: {basic_caption}"
                )
                text = generate_text(prompt, max_new_tokens=80)
                print(force_word_count(text, 50))

            elif choice == "4":
                print(f"{Fore.GREEN}Goodbye!")
                break
            
            else:
                print(f"{Fore.RED}Invalid choice")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Interrupted by user. Exiting.")

if __name__ == "__main__":
    main()