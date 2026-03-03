# ==========================================
# image_fetcher.py
# ==========================================
import requests, base64, time
from PIL import Image
from io import BytesIO

MAX_WIDTH = 720
MAX_HEIGHT = 1280

def fetch_free_image(prompt, save_path, max_attempts=3):
    API_URL = "https://hf.space/embed/stabilityai/stable-diffusion/api/predict/"
    headers = {"Accept": "application/json"}
    payload = {"data": [prompt]}
    attempt = 0
    while attempt < max_attempts:
        try:
            r = requests.post(API_URL, json=payload, headers=headers, timeout=60)
            if r.status_code != 200: raise Exception(f"Status code {r.status_code}")
            data = r.json()
            image_bytes = base64.b64decode(data['data'][0].split(",")[-1])
            img = Image.open(BytesIO(image_bytes))
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
            img.save(save_path)
            return save_path
        except Exception as e:
            attempt += 1
            print(f"[Attempt {attempt}] Image generation failed for prompt: '{prompt}'. Error: {e}")
            time.sleep(5)
    
    # fallback
    print(f"All attempts failed. Using placeholder for prompt: '{prompt}'")
    r = requests.get(f"https://via.placeholder.com/{MAX_WIDTH}x{MAX_HEIGHT}.png?text=Image+Error", timeout=10)
    with open(save_path, "wb") as f: f.write(r.content)
    return save_path