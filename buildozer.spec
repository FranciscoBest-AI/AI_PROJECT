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
requirements = python3,kivy,random

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) App icon (optional, place icon.png in project root)
icon.filename = %(source.dir)s/icon.png

# (str) Version of your app
version = 1.0.0

# (int) Android API level
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# (bool) Include Java/Kotlin support
android.archive = 1

# (str) Permissions your app may need
android.permissions = INTERNET

# (int) Logging level (optional, 2 = info)
log_level = 2