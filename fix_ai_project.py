import os
import subprocess
import sys

project_path = os.path.dirname(os.path.abspath(__file__))

# --- 1. Replace problematic_file.py with Flask ---
flask_code = """
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(\"\"\"
        <h1>Welcome to Your AI Project Flask App!</h1>
        <p>This is running successfully in AI_PROJECT.</p>
    \"\"\")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
"""

problematic_file_path = os.path.join(project_path, "problematic_file.py")
with open(problematic_file_path, "w") as f:
    f.write(flask_code)
print("[OK] Replaced problematic_file.py with Flask app.")

# --- 2. Check required packages ---
required_packages = ["flask", "requests", "pandas", "numpy"]
missing_packages = []

print("\n--- Checking Python Packages ---")
for pkg in required_packages:
    try:
        __import__(pkg)
        print(f"[OK] Package '{pkg}' is installed.")
    except ImportError:
        print(f"[MISSING] Package '{pkg}' is NOT installed!")
        missing_packages.append(pkg)

if missing_packages:
    print("\n⚠️ Missing packages detected!")
    print("⚠️ On Android (Pydroid), please open Pip → Search & Install the following packages:")
    for pkg in missing_packages:
        print(f"  - {pkg}")

# --- 3. Test running Python scripts ---
print("\n--- Testing Python Scripts ---")
for file in os.listdir(project_path):
    if file.endswith(".py") and file not in ["fix_ai_project.py"]:
        print(f"\nRunning {file}...")
        try:
            result = subprocess.run(
                [sys.executable, file],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"[OK] {file} ran successfully.")
            else:
                print(f"[ERROR] {file} returned an error:")
                print(result.stderr)
        except Exception as e:
            print(f"[ERROR] {file} could not run: {e}")

print("\n✅ AI_PROJECT fix and check complete!")