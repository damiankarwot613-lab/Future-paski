[app]

title = Paski Future
package.name = paski
package.domain = org.future

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx,csv
source.include_patterns = assets/*,data/*

version = 1.0

requirements = python3,kivy,pandas,openpyxl

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 23
android.ndk = 25b
android.ndk_api = 23

android.permissions = INTERNET

android.archs = arm64-v8a

android.private_storage = True

log_level = 2
