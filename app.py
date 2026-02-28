# ==========================================
# Niches & Ideas
# ==========================================

from flask import Flask, jsonify, render_template_string
import random
import csv
from datetime import datetime, timedelta

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

# ==========================================
# Advanced Content Generator
# ==========================================

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

# ==========================================
# Content Manager
# ==========================================

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

    def export_csv(self, filename):
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Type", "Hook", "Script", "CTA", "Caption", "Hashtags"])
            for c in self.contents:
                writer.writerow([
                    c.get("type"), c.get("hook"), c.get("script"),
                    c.get("cta"), c.get("caption"), c.get("hashtags")
                ])

    def schedule_posts(self, user_name):
        today = datetime.now()
        schedule = []
        for i, content in enumerate(self.contents, start=1):
            post_day = today + timedelta(days=i)
            schedule.append(f"{post_day.strftime('%Y-%m-%d')}: {content['type']}")
        return schedule

    def ask_ai(self, niche, style, user_name):
        return f"AI suggestion for {niche} ({style}) for {user_name}"

# ==========================================
# Flask App
# ==========================================

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
</body>
</html>
"""

@app.route("/")
def home():
    manager.generate_daily_content()
    return render_template_string(HTML_PAGE, contents=manager.show_contents())

# ------------------------------
# Keep Original API Access
# ------------------------------

@app.route("/api")
def api_contents():
    return jsonify({"contents": manager.show_contents()})

@app.route("/export")
def export_csv_route():
    manager.export_csv("Daily_Content_Terminal.csv")
    return jsonify({"status": "CSV exported successfully!"})

@app.route("/suggest/<niche>/<style>/<user_name>")
def suggest_route(niche, style, user_name):
    suggestion = manager.ask_ai(niche, style, user_name)
    return jsonify({"suggestion": suggestion})

@app.route("/healthz")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)