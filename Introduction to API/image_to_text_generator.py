import requests

MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
API_URL = f"https://router.huggingface.co/hf-inference/models/Salesforce/blip-image-captioning-basehttps://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {
    "Authorization": f"Bearer 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",
    "Content-Type": "application/json"
}

def captions_single_image():
    with open("picture.jpg", "rb") as f:
        image_bytes = f.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "inputs": image_base64
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("Status:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        result = response.json()
        print("Caption:", result[0]["generated_text"])
    else:
        print("Error:", response.json())

def main():
    captions_single_image()

if __name__ == "__main__":
    main()