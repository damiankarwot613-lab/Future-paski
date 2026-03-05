[app]

title = ExcelExporterUltra
package.name = excelexporter
package.domain = org.private

source.dir = .
source.include_exts = py,xls,xlsx

version = 1.0

requirements = python3,kivy,pandas,openpyxl,plyer,cython

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.accept_sdk_license = True

log_level = 2

[buildozer]

log_level = 2
warn_on_root = 1
