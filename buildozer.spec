[app]

title = Excel Exporter
package.name = excelexporter
package.domain = org.test

source.dir = .
source.include_exts = py,xls,xlsx

version = 1.0

requirements = python3,kivy,pandas,openpyxl,cython,numpy

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b
android.arch = armeabi-v7a

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.accept_sdk_license = True

log_level = 2

warn_on_root = 1

[buildozer]

log_level = 2
warn_on_root = 1
