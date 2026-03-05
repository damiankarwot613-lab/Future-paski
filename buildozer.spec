[app]

title = ExcelExporter
package.name = excelexporter
package.domain = org.private

source.dir = .
source.include_exts = py,png,jpg,kv,xlsx,xls,csv

version = 1.0

requirements = python3,kivy,pandas,openpyxl,numpy

orientation = portrait

fullscreen = 0

# brak ikon
icon.filename = 

# brak presplash
presplash.filename = 

# katalog assets
source.include_dirs = assets

# permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# Android API
android.api = 33
android.minapi = 24
android.ndk_api = 24

# architektura
android.archs = arm64-v8a,armeabi-v7a

# build tools
android.gradle_dependencies =

# python for android
p4a.branch = master

# log
log_level = 2

# build dir
build_dir = .buildozer

# assets
android.add_assets = assets

# encoding
android.encoding = utf-8

# allow backup
android.allow_backup = True

# fullscreen
android.fullscreen = False

# window
android.window.softinput_mode = resize

# numeric version
version.code = 1

# services
services =

# whitelist
android.whitelist =

# ndk
android.ndk = 25b

# sdk
android.sdk = 33

# update behaviour
android.update_sdk = True
android.accept_sdk_license = True

# debug
android.debug = False

# strip
android.strip_debug_symbols = True

# copy libs
android.copy_libs = True

# bootstrap
p4a.bootstrap = sdl2

# compile options
android.enable_androidx = True

# storage
android.storage = auto

# build mode
android.release_artifact = apk

# keystore (niepotrzebny prywatnie)
android.release_keystore =

# extra
android.logcat_filters = *:S python:D

# entrypoint
entrypoint = main.py
