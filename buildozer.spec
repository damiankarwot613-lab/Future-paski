[app]

# (str) Title of your application
title = Ultra Exporter

# (str) Package name
package.name = ultraexport

# (str) Package domain
package.domain = org.private

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,plyer,openpyxl

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2


# Android specific
# ------------------------------------------------

# Target Android API
android.api = 33

# Minimum API your APK will support
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Android NDK API
android.ndk_api = 21

# Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# Android permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Automatically accept SDK licenses
android.accept_sdk_license = True

# Store app data privately
android.private_storage = True

# Orientation
android.orientation = portrait

# Copy python libs
android.copy_libs = 1


# Python for Android
# ------------------------------------------------

p4a.bootstrap = sdl2


# Debug
# ------------------------------------------------

android.logcat_filters = *:S python:D


# Build directory
build_dir = .buildozer


# Gradle dependencies
android.gradle_dependencies =


# End of configuration
