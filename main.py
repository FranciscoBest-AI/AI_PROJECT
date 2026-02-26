from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

# ===============================
# Your AI Logic (from Flask app)
# ===============================
# Example: replace Flask routes with functions
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

def generate_idea(category):
    """Return a random idea from a niche"""
    import random
    if category in niches_ideas:
        return random.choice(niches_ideas[category])
    return "No ideas available"

# ===============================
# Kivy App
# ===============================
class AIContentManagerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Welcome to AI Content Manager", size_hint_y=None, height=50)
        self.layout.add_widget(self.label)

        # Buttons for each niche
        for niche in niches_ideas.keys():
            btn = Button(text=f"Generate {niche} Idea", size_hint_y=None, height=40)
            btn.bind(on_press=self.make_generate_function(niche))
            self.layout.add_widget(btn)

        # Scrollable area for output
        self.scroll = ScrollView(size_hint=(1, None), size=(self.layout.width, 200))
        self.output_label = Label(text="", size_hint_y=None)
        self.output_label.bind(texture_size=self.output_label.setter('size'))
        self.scroll.add_widget(self.output_label)
        self.layout.add_widget(self.scroll)

        return self.layout

    def make_generate_function(self, niche):
        # Return a function that updates output_label when button pressed
        def generate(instance):
            idea = generate_idea(niche)
            self.output_label.text += f"{niche}: {idea}\n"
        return generate

if __name__ == '__main__':
    AIContentManagerApp().run()