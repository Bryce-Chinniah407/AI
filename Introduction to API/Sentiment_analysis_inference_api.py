import requests

def classify_text(text):
    HF_API_KEY ="API_KEY_HERE"
    API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)


    if response.status_code == 200:
        return response.json()
    
    else:
        print("Request Failed")
        return None

while True:    
    intrigue = input("Type 'm' to continue or 'q' to exit:  ")
    if intrigue == "m":
        sample_text = input("Enter a Phrase to analyse how you are feeling: ")
        result = classify_text(sample_text)
        print(result)

    elif intrigue == "q":
        break
    else:
        print("Invalid Input")

