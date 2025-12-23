import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

def generate_image_from_Text(prompt):
    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer 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"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    
    else:
        raise Exception(f"Requests failed with status code {response.status_code}: {response.text}")
    
def post_process_image(image, Style):
    if Style == "day" or Style == "daylight":
        enhancer = ImageEnhance.Brightness(image)
        bright_image = enhancer.enhance(1.0)

        enhancer = ImageEnhance.Contrast(bright_image)
        contrast_image = enhancer.enhance(0.7)
        soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=2))
    elif Style == "night":
        enhancer = ImageEnhance.Brightness(image)
        new_image = enhancer.enhance(0.1)

        enhancer = ImageEnhance.Contrast(new_image)
        contrast_image = enhancer.enhance(4.0)
        soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=1))
    else:
        enhancer = ImageEnhance.Brightness(image)
        bright_image = enhancer.enhance(1.3)

        enhancer = ImageEnhance.Contrast(bright_image)
        contrast_image = enhancer.enhance(1.2)
        soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=1))

    return soft_focus_image

def  main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image from text and applies post-processing effects.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a description for the image(Or 'exit' to quit.)\n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            print("exiting...")
            break
        try:
            print("\nGenerating image...")
            image = generate_image_from_Text(user_input)
            print("Would you like to use a daylight filter or a night filter\n")
            style = input(">  ").strip().lower()
            print("Applying post-processing effects...\n")
            processed_image = post_process_image(image, style)
            processed_image.show()

            save_option = input("Do you want to save this image(yes/no):    ").strip().lower()
            if save_option == 'yes':
                file_name = input("enter a name for the image file (without extension): ").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")
            print("--" * 80 + "\n")

        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()

