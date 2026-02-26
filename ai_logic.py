# ai_logic.py
import random

# AI niches and ideas
niches_ideas = {
    "Sculpture Carving": [
        "Full Process Sculpture",
        "Wood Carving Tips"
    ],
    "Painting": [
        "Watercolor Techniques",
        "Oil Painting Tutorials"
    ]
}

# Function to generate an idea from a niche
def generate_idea(category):
    """Return a random idea from a niche"""
    if category in niches_ideas:
        return random.choice(niches_ideas[category])
    return "No ideas available"