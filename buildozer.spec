[app]

# (str) Title of your application
title = Joy Calculator

# (str) Package name
package.name = joycalculator

# (str) Package domain
package.domain = org.joy

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude
source.exclude_exts = spec

# (list) Exclude directories
source.exclude_dirs = tests, bin, venv

# (list) Exclude patterns
source.exclude_patterns = license,images/*/*.jpg

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash
presplash.filename =

# (str) Icon
icon.filename =

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Android permissions
android.permissions = INTERNET

# (int) Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android SDK
android.sdk = 20

# (str) Android NDK version
android.ndk = 25b

# (bool) Use AndroidX
android.enable_androidx = True

# (list) Architecture
android.archs = arm64-v8a, armeabi-v7a

# (str) Entry point
entrypoint = org.kivy.android.PythonActivity

# (str) Splash screen color
android.presplash_color = #FFFFFF

# (bool) Wake lock
android.wakelock = False

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) Log level
log_level = 2

# (bool) Copy libs
copy_libs = 1

# (bool) Warn on root
warn_on_root = 1

#
# Python for Android
#

# Bootstrap
p4a.bootstrap = sdl2

# Extra arguments for p4a
p4a.extra_args =

# Local recipes
p4a.local_recipes =

# Local requirements
p4a.local_requirements =

#
# Build options
#

build_dir = .buildozer

bin_dir = ./bin

# Enable ccache
ccache = 0

# Number of build jobs
build_jobs = 4

#
# Android options
#

android.release_artifact = apk

android.debug_symbols = False

android.copy_libs = 1

android.numeric_version = 1

android.manifest.intent_filters =

android.add_gradle_repositories =

android.add_packaging_options =

android.gradle_dependencies =

android.add_aars =

android.whitelist =

#
# Buildozer settings
#

# Build mode
build_mode = debug

# Storage location
android.private_storage = True

# Keep screen on
android.wakelock = False

# Backup rules
android.allow_backup = True

# App theme
android.theme = Theme.NoTitleBar

# Window soft input mode
android.window_softinput_mode = adjustResize

#
# Logging
#

log_level = 2

#
# End of configuration
