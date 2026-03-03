# ==========================================
# image_fetcher.py (Optimized Version)
# ==========================================

import requests
import base64
import time
from PIL import Image
from io import BytesIO

MAX_WIDTH = 720
MAX_HEIGHT = 1280

def fetch_free_image(prompt, save_path, max_attempts=3):
    """
    Fetch AI-generated image from Hugging Face Stable Diffusion space.
    Saves the image to save_path.
    Optimized for 720x1280 vertical videos and stable retries.
    """
    API_URL = "https://hf.space/embed/stabilityai/stable-diffusion/api/predict/"
    headers = {"Accept": "application/json"}
    payload = {"data": [prompt]}

    attempt = 0
    while attempt < max_attempts:
        try:
            response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
            if response.status_code != 200:
                raise Exception(f"Status code {response.status_code}")
            data = response.json()
            image_base64 = data['data'][0].split(",")[-1]
            image_bytes = base64.b64decode(image_base64)

            # Open image with PIL and resize to MAX_WIDTH x MAX_HEIGHT if needed
            img = Image.open(BytesIO(image_bytes))
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
            img.save(save_path)

            return save_path

        except Exception as e:
            attempt += 1
            print(f"[Attempt {attempt}] Image generation failed for prompt: '{prompt}'. Error: {e}")
            time.sleep(5)

    # Fallback placeholder if all attempts fail
    print(f"All attempts failed. Using placeholder for prompt: '{prompt}'")
    placeholder_url = f"https://via.placeholder.com/{MAX_WIDTH}x{MAX_HEIGHT}.png?text=Image+Error"
    try:
        r = requests.get(placeholder_url, timeout=10)
        with open(save_path, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"Placeholder download failed: {e}")

    return save_path