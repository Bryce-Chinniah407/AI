import requests
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://router.huggingface.co/hf-inference/models/{model_name}"

def query(payload, model_name=DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer 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"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    payload = {"inputs": text, "parameters": {"min_length": min_length, "max_length": max_length}}

    print(Fore.BLUE + Style.BRIGHT + f"\n???? performing AI summarization using models: {model_name}")
    result = query(payload, model_name=model_name)
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "❌ Error in summarisation response: ", result)
        return None
    
if __name__