# ==========================================
# app.py (BACKGROUND VIDEO VERSION - SAFE)
# ==========================================

from flask import Flask, jsonify, render_template_string, request
import random
import os
import threading
import uuid
from datetime import datetime
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
    def generate_full_process_script(self, niche):
        hook = f"This {niche.lower()} will become something amazing!"

        if niche == "Sculpture Carving":
            script_steps = [
                "Step 1: I mark the proportions carefully.",
                "Step 2: I remove excess wood.",
                "Step 3: I shape the structure.",
                "Step 4: I carve fine details.",
                "Step 5: I polish and finish."
            ]
            hashtags = "#Sculpture #WoodCarving #ArtProcess"

        elif niche == "Car Building":
            script_steps = [
                "Step 1: Inspect the frame.",
                "Step 2: Disassemble old parts.",
                "Step 3: Repair components.",
                "Step 4: Reassemble engine.",
                "Step 5: Final detailing."
            ]
            hashtags = "#CarRestoration #DIYCar #Engineering"

        else:
            script_steps = ["Step 1: Start project.", "Step 2: Continue..."]
            hashtags = "#CreativeProcess"

        script = "\n".join(script_steps)

        return {
            "type": f"{niche} Full Process",
            "hook": hook,
            "script": script,
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
# Flask Setup
# ------------------------------

app = Flask(__name__)
manager = ContentManager(niches_ideas)
manager.generate_daily_content()

# In-memory job tracking
video_jobs = {}

# Ensure folders exist
os.makedirs("static/videos", exist_ok=True)
os.makedirs("static/images", exist_ok=True)

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
        <pre>{{ content.script }}</pre>
        <hr>
    {% endfor %}

    <h2>🎬 Generate Video (15-30 sec)</h2>
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
    document.getElementById("status").innerText = "Starting video generation...";

    fetch("/generate-video", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "niche": niche })
    })
    .then(res => res.json())
    .then(data => {
        checkStatus(data.job_id);
    });
}

function checkStatus(jobId) {
    fetch("/video-status/" + jobId)
    .then(res => res.json())
    .then(data => {
        if (data.status === "processing") {
            document.getElementById("status").innerText = "Rendering video...";
            setTimeout(() => checkStatus(jobId), 5000);
        } 
        else if (data.status === "completed") {
            document.getElementById("status").innerText = "Video ready!";
            const video = document.getElementById("videoPreview");
            video.src = data.video_url + "?t=" + new Date().getTime();
            video.style.display = "block";

            const link = document.getElementById("downloadLink");
            link.href = data.video_url;
            link.style.display = "inline";
        } 
        else {
            document.getElementById("status").innerText = "Video failed.";
        }
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
# Background Video Processor
# ------------------------------

def process_video_job(job_id, niche_name):
    try:
        scenes = [
            "Workshop setup",
            "Shaping process",
            "Detail carving",
            "Sanding and smoothing",
            "Final reveal"
        ]

        images = []
        for i, scene in enumerate(scenes):
            prompt = f"Vertical 9:16 realistic {niche_name} {scene}, cinematic lighting"
            img_path = fetch_free_image(prompt, f"static/images/{job_id}_{i}.png")
            images.append(img_path)

        video_filename = f"{job_id}.mp4"
        video_path = f"static/videos/{video_filename}"

        create_video_from_images(
            images,
            video_path,
            duration_per_scene=5,      # 5 sec × 5 scenes = 25 sec
            resolution=(720, 1280)     # 720p vertical
        )

        video_jobs[job_id] = {
            "status": "completed",
            "video_url": f"/static/videos/{video_filename}"
        }

    except Exception as e:
        video_jobs[job_id] = {
            "status": "failed",
            "error": str(e)
        }

# ------------------------------
# Routes
# ------------------------------

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.get_json()
    niche_type = data.get("niche", "Sculpture Carving Full Process")
    niche_name = niche_type.split(" Full Process")[0]

    job_id = str(uuid.uuid4())
    video_jobs[job_id] = {"status": "processing"}

    thread = threading.Thread(target=process_video_job, args=(job_id, niche_name))
    thread.start()

    return jsonify({"job_id": job_id})

@app.route("/video-status/<job_id>")
def video_status(job_id):
    job = video_jobs.get(job_id)
    if not job:
        return jsonify({"error": "Invalid job ID"}), 404
    return jsonify(job)

@app.route("/healthz")
def health_check():
    return {"status": "ok"}

# ------------------------------
# Run Local Only
# ------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)