[app]

title = Excel Exporter ULTRA
package.name = excelexporter
package.domain = org.private

source.dir = .
source.include_exts = py,png,jpg,kv,xls,xlsx

version = 1.0

orientation = portrait

fullscreen = 0

requirements = python3,kivy,cython,pyjnius,pandas,openpyxl

log_level = 2

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25c
android.ndk_api = 21

android.accept_sdk_license = True

android.enable_androidx = True

android.gradle_dependencies = androidx.documentfile:documentfile:1.0.1

p4a.branch = develop

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.private_storage = False

android.release_artifact = apk

android.debug_artifact = apk

android.manifest.intent_filters =

android.add_assets = assets

[buildozer]

log_level = 2

warn_on_root = 1
