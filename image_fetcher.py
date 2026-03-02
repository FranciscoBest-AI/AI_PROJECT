import requests
import base64
import time

def fetch_free_image(prompt, save_path):
    """
    Fetch AI-generated image from Hugging Face Stable Diffusion space.
    Saves the image to save_path.
    """
    try:
        # Public inference API for SD
        API_URL = "https://hf.space/embed/stabilityai/stable-diffusion/api/predict/"
        headers = {"Accept": "application/json"}

        payload = {"data": [prompt]}
        response = requests.post(API_URL, json=payload, headers=headers, timeout=60)

        # Sometimes free space takes a while
        attempts = 0
        while response.status_code != 200 and attempts < 3:
            time.sleep(5)
            response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
            attempts += 1

        data = response.json()
        image_base64 = data['data'][0].split(",")[-1]
        image_bytes = base64.b64decode(image_base64)

        with open(save_path, "wb") as f:
            f.write(image_bytes)

        return save_path

    except Exception as e:
        print(f"Image generation failed for prompt: {prompt}, Error: {e}")
        # Fallback placeholder
        placeholder_url = "https://via.placeholder.com/1080x1920.png?text=Image+Error"
        r = requests.get(placeholder_url)
        with open(save_path, "wb") as f:
            f.write(r.content)
        return save_path