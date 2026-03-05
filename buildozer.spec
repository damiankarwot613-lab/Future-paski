[app]

title = ExcelExporter
package.name = excelexporter
package.domain = org.test

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy==2.2.1,pandas==1.5.3,openpyxl==3.1.2,plyer,cython==0.29.36

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.archs = arm64-v8a,armeabi-v7a

p4a.bootstrap = sdl2

log_level = 2

warn_on_root = 1
