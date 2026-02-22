import random
import csv
from datetime import datetime, timedelta

# ==========================================
# Advanced Local AI Content System
# ==========================================

class AdvancedContentGenerator:
    def __init__(self):
        self.viral_tags = [
            "#ViralNow", "#Trending", "#MustWatch",
            "#ExplosiveGrowth", "#NextLevel", "#Dominate",
            "#AlgorithmBoost", "#ContentKing"
        ]

    # Generate hashtags for each niche
    def generate_hashtags(self, niche):
        niche_tag = "#" + niche.replace(" ", "")
        selected = random.sample(self.viral_tags, 4)
        return niche_tag + " " + " ".join(selected)

    # 45-Minute Deep Video Structure
    def generate_long_video(self, idea):
        title = f"Mastering {idea}: 45-Minute Deep Dive"
        outline = [
            "🔥 Hook & Big Promise (5 min)",
            "📚 Background & Context (10 min)",
            "🛠 Core Techniques Explained (15 min)",
            "🚀 Advanced Strategies (10 min)",
            "🎯 Final Action Plan & Call To Action (5 min)"
        ]
        description = f"This deep 45-minute session reveals powerful strategies about {idea} to help you dominate your space."
        return {
            "type": "45-Min Video",
            "title": title,
            "details": " | ".join(outline),
            "description": description,
            "hashtags": self.generate_hashtags(idea)
        }

    # 20-Second Reel Script
    def generate_reel(self, idea):
        title = f"20-Second {idea} Hack That Changes Everything"
        script = [
            "0-3s: Powerful Hook",
            "3-10s: Quick Insight",
            "10-17s: Fast Demonstration",
            "17-20s: Strong Call To Action"
        ]
        description = f"A fast 20-second reel delivering instant value about {idea}."
        return {
            "type": "20-Second Reel",
            "title": title,
            "details": " | ".join(script),
            "description": description,
            "hashtags": self.generate_hashtags(idea)
        }

    # Image + Riddle
    def generate_image_riddle(self, idea):
        riddle = f"I grow in {idea}, yet I have no roots. I inspire millions but have no voice. What am I?"
        caption = f"Can you solve this {idea} riddle? Drop your answer below!"
        return {
            "type": "Image with Riddle",
            "title": riddle,
            "details": caption,
            "description": "Engagement boosting riddle post.",
            "hashtags": self.generate_hashtags(idea)
        }

# ==========================================
# Content Manager
# ==========================================

class ContentManager:
    def __init__(self, niches_ideas):
        self.niches_ideas = niches_ideas
        self.generator = AdvancedContentGenerator()
        self.contents = []

    # Generate all daily content for all niches
    def generate_daily_content(self):
        for niche, ideas in self.niches_ideas.items():
            for idea in ideas:
                # 2 Long Videos
                for _ in range(2):
                    self.contents.append(self.generator.generate_long_video(idea))
                # 4 Reels
                for _ in range(4):
                    self.contents.append(self.generator.generate_reel(idea))
                # 2 Images with Riddles
                for _ in range(2):
                    self.contents.append(self.generator.generate_image_riddle(idea))
        print("\n✅ Daily Content Generated Successfully!\n")

    # Show generated content
    def show_content(self):
        for content in self.contents:
            print("\n------------------------------")
            print("Type:", content["type"])
            print("Title:", content["title"])
            print("Structure/Script:", content["details"])
            print("Description:", content["description"])
            print("Hashtags:", content["hashtags"])

    # Export content to CSV
    def export_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Title", "Details", "Description", "Hashtags"])
            for content in self.contents:
                writer.writerow([
                    content["type"],
                    content["title"],
                    content["details"],
                    content["description"],
                    content["hashtags"]
                ])
        print(f"\n📁 Exported to {filename}")

    # Simulate posting schedule for social media
    def simulate_schedule(self):
        schedule = []
        post_time = datetime.now()
        for content in self.contents:
            schedule.append({
                "time": post_time.strftime("%Y-%m-%d %H:%M"),
                "platforms": ["Facebook", "Instagram", "YouTube", "TikTok"],
                "type": content["type"],
                "title": content["title"]
            })
            post_time += timedelta(hours=2)  # every 2 hours for simulation
        print("\n🗓 Scheduled Posts:")
        for s in schedule:
            print(s)

# ==========================================
# NICHES & IDEAS
# ==========================================
niches_ideas = {
    "Sculpture Carving": [
        "Young boy carving human on tree",
        "Young boy carving human with snow (realistic ice sculpture)",
        "Young boy carving human with wood",
        "Young boy building house from coconut fronds",
        "Young boy building car from coconut tree leaves"
    ],
    "AI Content Creation": [
        "Old man giving audience advice",
        "Old man teaching success",
        "Old man blessing people"
    ],
    "Digital Art": [
        "Futuristic city skyline",
        "Magical forest with creatures",
        "Cyberpunk character portrait"
    ],
    "Pencil Drawing and Painting": [
        "Realistic portrait of a girl reading",
        "Detailed sketch of an old town street",
        "Nature landscape with shadows and light"
    ]
}

# ==========================================
# RUN
# ==========================================
manager = ContentManager(niches_ideas)
manager.generate_daily_content()
manager.show_content()
manager.export_csv("Daily_Content.csv")
manager.simulate_schedule()