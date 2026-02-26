[app]

# (str) Title of your application
title = AI Content Manager

# (str) Package name
package.name = aicontentmanager

# (str) Package domain (unique)
package.domain = org.francis

# (str) Source code folder
source.dir = .

# (str) Main Python file to run
source.main = main.py

# (list) File extensions to include
source.include_exts = py,png,jpg,kv,json

# (list) Python modules your app uses
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) App icon (optional, place icon.png in project root)
icon.filename = %(source.dir)s/icon.png

# (str) Version of your app
version = 1.0.0

# -----------------------------
# ANDROID SETTINGS (STABLE)
# -----------------------------

# Android API to use
android.api = 33

# Minimum Android API
android.minapi = 21

# Target SDK
android.sdk = 33

# NDK version
android.ndk = 25b

# Force stable build tools (VERY IMPORTANT)
android.sdk_build_tools = 33.0.2

# Permissions
android.permissions = INTERNET

# Logging level
log_level = 2