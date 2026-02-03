import streamlit as st
import re
from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI

client = OpenAI(api_key="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")

def is_prompt_safe(prompt: str) -> bool:
    forbidden_keywords = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex", "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
    ]
    pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)
    return not bool(pattern.search(prompt))

def generate_image(prompt: str, size: str = "1024x1024"):
    if not is_prompt_safe(prompt):
        return None, "⚠️ Your  prompt contains restricted or unsafe content."
    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size
        )

        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_bytes))

        return image, None
    
    except Exception as e:
        return None, f"❌ Image generation failed: {e}"
    

st.set_page_config(page_title="Safe AI Image Generator (OpenAI)", layout="centered")

st.title("🖼️ Safe AI Image Generator (OpenAI)")

st.write(
    "Enter a description to generate a safe AI image using OpenAI.\n\n"
    "Examples:\n"
    "- A serene sunset over a mountain lake\n"
    "- A futuristic city skyline at night\n"
    "- A cyberpunk robot walking in the rain"
)

with st.form(key="Image_gen_form"):
    prompt = st.text_area(
        "Image Description:",
        height=120,
        placeholder="Describe the image you want to ganerate... be specific for better results!"
    )

    submit = st.form_submit_button("Generate Image")

    if submit:
        if not prompt.strip():
            st.warning("⚠️ Please enter an image description.")

        else:
            with st.spinner("Generating image..."):
                image, error = generate_image(prompt.strip())

            if error:
                st.error(error)
            elif image:
                st.image(image, caption="Generate Image", use_container_width=True)
                st.session_state.generate_image = image
            else:
                st.error("Failed to generate image. Please try again.")

if hasattr(st.session_state, "generate_image") and st.session_state.generate_image:
    buf = BytesIO()
    st.session_state.generatef_image.save(buf, format='PNG')
    byte_im = buf.getvalue()

    st.download_button(
        label="⬇️ Download Genrated Image",
        data=byte_im,
        file_name="ai_generated_image.png",
        mime="image/png",
        help="Click to download the generated image"
    )