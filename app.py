# ==========================================
# app.py (Updated Version)
# ==========================================

from flask import Flask, jsonify, render_template_string, request, send_from_directory
import random
import csv
import os
from datetime import datetime, timedelta
from video_generator import create_video_from_images
from image_fetcher import fetch_free_image

# ------------------------------
# Niches & Ideas
# ------------------------------
niches_ideas = {
    "Sculpture Carving": [
        "Full Process Sculpture",
        "Wood Carving Tips",
        "Step-by-Step Human Sculpture"
    ],
    "Car Building": [
        "DIY Car Restoration",
        "Engine Tuning Tips",
        "Custom Modifications"
    ]
}

# ------------------------------
# Advanced Content Generator
# ------------------------------

class AdvancedContentGenerator:
    def motivate(self):
        motivations = [
            "Keep building your skills daily!",
            "Patience turns ideas into masterpieces.",
            "Consistency is the secret to mastery.",
            "Every small step creates big results."
        ]
        return random.choice(motivations)

    def generate_full_process_script(self, niche):
        hook = f"This {niche.lower()} will become something amazing!"

        if niche == "Sculpture Carving":
            script_steps = [
                "Step 1: I mark the proportions carefully.",
                "Step 2: I remove the excess wood using my chisel.",
                "Step 3: I begin shaping the body structure.",
                "Step 4: I carve the facial details.",
                "Step 5: I smooth and polish the surface.",
                "Step 6: Final touch-ups to make it perfect."
            ]
            hashtags = "#Sculpture #WoodCarving #ArtProcess #AfricanArt"

        elif niche == "Car Building":
            script_steps = [
                "Step 1: I inspect the car frame.",
                "Step 2: I disassemble old parts carefully.",
                "Step 3: I repair and replace components.",
                "Step 4: I assemble the engine and systems.",
                "Step 5: I paint and detail the car.",
                "Step 6: Final testing and adjustments."
            ]
            hashtags = "#CarRestoration #DIYCar #Engineering #CarMods"

        else:
            script_steps = ["Step 1: Start the project...", "Step 2: Continue..."]
            hashtags = "#CreativeProcess"

        script = "\n".join(script_steps)
        cta = "Follow to see the final result!"
        caption = f"From start to finish, watch this {niche.lower()} come alive."

        return {
            "type": f"{niche} Full Process",
            "hook": hook,
            "script": script,
            "cta": cta,
            "caption": caption,
            "hashtags": hashtags
        }

# ------------------------------
# Content Manager
# ------------------------------

class ContentManager:
    def __init__(self, niches):
        self.niches = niches
        self.contents = []
        self.generator = AdvancedContentGenerator()

    def generate_daily_content(self):
        self.contents = []
        for niche in self.niches:
            content = self.generator.generate_full_process_script(niche)
            self.contents.append(content)

    def show_contents(self):
        return self.contents

# ------------------------------
# Flask App Setup
# ------------------------------

app = Flask(__name__)
manager = ContentManager(niches_ideas)
manager.generate_daily_content()

# ------------------------------
# Web Interface
# ------------------------------

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Francis AI Content Manager</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h1>Francis AI Content Manager 🚀</h1>
    <p>Your AI is live and running.</p>
    <hr>

    {% for content in contents %}
        <h2>{{ content.type }}</h2>
        <strong>Hook:</strong>
        <p>{{ content.hook }}</p>

        <strong>Script:</strong>
        <pre>{{ content.script }}</pre>

        <strong>CTA:</strong>
        <p>{{ content.cta }}</p>

        <strong>Caption:</strong>
        <p>{{ content.caption }}</p>

        <strong>Hashtags:</strong>
        <p>{{ content.hashtags }}</p>

        <hr>
    {% endfor %}

    <h2>🎬 Generate Sculpture Video</h2>
    <select id="niche">
        {% for niche in contents %}
            <option value="{{ niche.type }}">{{ niche.type }}</option>
        {% endfor %}
    </select>
    <button onclick="generateVideo()">Generate Video</button>
    <p id="status"></p>
    <video id="videoPreview" width="360" height="640" controls style="display:none;"></video>
    <a id="downloadLink" href="" download style="display:none;">Download Video</a>

<script>
function generateVideo() {
    const niche = document.getElementById("niche").value;
    document.getElementById("status").innerText = "Generating video, please wait...";

    fetch("/generate-video", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "niche": niche })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = "Video ready!";
        const video = document.getElementById("videoPreview");
        video.src = data.video_url + "?t=" + new Date().getTime();
        video.style.display = "block";

        const link = document.getElementById("downloadLink");
        link.href = data.video_url;
        link.style.display = "inline";
    });
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    manager.generate_daily_content()
    return render_template_string(HTML_PAGE, contents=manager.show_contents())

# ------------------------------
# Original API Routes
# ------------------------------

@app.route("/api")
def api_contents():
    return jsonify({"contents": manager.show_contents()})

# ------------------------------
# NEW: Generate Video Route
# ------------------------------

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.get_json()
    niche_type = data.get("niche", "Sculpture Carving Full Process")

    # Find the niche name from type
    niche_name = niche_type.split(" Full Process")[0]

    # Scene breakdown (8 scenes)
    scenes = [
        "Raw wood block on workbench",
        "Rough shaping with chisel",
        "Face detailing",
        "Hand shaping",
        "Fine carving details",
        "Sanding process",
        "Applying oil finish",
        "Final polished sculpture reveal"
    ]

    # Generate prompts for each scene
    image_prompts = [
        f"Vertical 9:16 realistic {niche_name} carving workshop, {scene}, cinematic lighting, detailed wood texture"
        for scene in scenes
    ]

    # Fetch images (using free image platform)
    images = []
    for i, prompt in enumerate(image_prompts):
        img_path = fetch_free_image(prompt, f"static/images/{niche_name.replace(' ', '_')}_{i+1}.png")
        images.append(img_path)

    # Create video
    video_filename = f"{niche_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
    video_path = f"static/videos/{video_filename}"
    create_video_from_images(images, video_path, duration_per_scene=7.5)

    video_url = f"/static/videos/{video_filename}"
    return jsonify({"video_url": video_url})

# ------------------------------
# Health Check
# ------------------------------
@app.route("/healthz")
def health_check():
    return {"status": "ok"}

# ------------------------------
# Run Flask App
# ------------------------------
if __name__ == "__main__":
    if not os.path.exists("static/videos"):
        os.makedirs("static/videos")
    if not os.path.exists("static/images"):
        os.makedirs("static/images")
    app.run(host="0.0.0.0", port=5000, debug=True)