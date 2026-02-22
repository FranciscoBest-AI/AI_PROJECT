# problematic_file.py
from flask import Flask, render_template_string

app = Flask(__name__)

# Simple home page
@app.route("/")
def home():
    return render_template_string("""
        <h1>Welcome to Your AI Project Flask App!</h1>
        <p>This is running successfully in AI_PROJECT.</p>
    """)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)