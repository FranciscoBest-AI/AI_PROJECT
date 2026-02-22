# check_ai_project.py
import os
import subprocess
import sys

project_path = os.path.dirname(os.path.abspath(__file__))

# --- 1. List all files ---
print("\n--- Project Files ---")
for root, dirs, files in os.walk(project_path):
    for file in files:
        print(os.path.relpath(os.path.join(root, file), project_path))

# --- 2. Check required Python packages ---
required_packages = ["flask", "requests", "pandas"]
print("\n--- Checking Python Packages ---")
for pkg in required_packages:
    try:
        __import__(pkg)
        print(f"[OK] Package '{pkg}' is installed.")
    except ImportError:
        print(f"[MISSING] Package '{pkg}' is NOT installed!")

# --- 3. Test running Python scripts ---
print("\n--- Testing Python Scripts ---")
for file in os.listdir(project_path):
    if file.endswith(".py") and file != "check_ai_project.py":
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

print("\n✅ AI_PROJECT check complete!")