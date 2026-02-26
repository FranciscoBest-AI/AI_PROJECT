import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class AIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="AI Content Manager")
        self.button = Button(text="Generate Content")

        self.button.bind(on_press=self.generate)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    def generate(self, instance):
        try:
            response = requests.get("https://your-backend-url.onrender.com/")
            self.label.text = response.text
        except:
            self.label.text = "Error connecting to AI"

AIApp().run()