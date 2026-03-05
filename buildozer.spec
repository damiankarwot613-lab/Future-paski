[app]

# (str) Title of your application
title = Paski Future

# (str) Package name
package.name = paski

# (str) Package domain
package.domain = org.future

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,xlsx,csv

# (list) Files to exclude
source.exclude_exts = spec

# (list) Excluded directories
source.exclude_dirs = tests, bin, venv

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pandas,openpyxl

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Presplash
#presplash.filename = assets/presplash.png

# (str) Icon
#icon.filename = assets/icon.png


# -------------------------------------------------
# ANDROID
# -------------------------------------------------

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (int) Android NDK API
android.ndk_api = 21

# (str) Android SDK
android.sdk = 33

# (str) Build tools
android.build_tools = 33.0.2

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# (list) Android features
android.features = android.hardware.touchscreen

# (bool) Enable AndroidX
android.enable_androidx = True

# (bool) Accept SDK licenses
android.accept_sdk_license = True


# -------------------------------------------------
# BUILD OPTIONS
# -------------------------------------------------

# (int) Log level
log_level = 2

# (bool) Warn on root
warn_on_root = 1

# (str) Architecture
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy libs
android.copy_libs = 1

# (bool) Use AAPT2
android.use_aapt2 = True

# (bool) Skip update
android.skip_update = False

# (bool) Private storage
android.private_storage = True


# -------------------------------------------------
# PYTHON
# -------------------------------------------------

# (str) Python version
osx.python_version = 3

# (str) Python branch
osx.kivy_version = 2.3.0


# -------------------------------------------------
# SERVICES
# -------------------------------------------------

# (list) Services
services =


# -------------------------------------------------
# DEBUG
# -------------------------------------------------

# (bool) Enable debug
android.debug = True


# -------------------------------------------------
# GRADLE
# -------------------------------------------------

android.gradle_dependencies =

android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"


# -------------------------------------------------
# ASSETS
# -------------------------------------------------

# (str) Extra source files
#android.add_src =


# -------------------------------------------------
# PACKAGE DATA
# -------------------------------------------------

# (list) Patterns
source.include_patterns = assets/*,data/*


# -------------------------------------------------
# END
# -------------------------------------------------
