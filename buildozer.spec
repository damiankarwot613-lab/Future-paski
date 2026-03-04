[app]

title = PaskiFuture
package.name = paskifuture
package.domain = org.paskifuture

source.include_exts = py,png,jpg,kv,json

requirements = python3,kivy==2.3.0,openpyxl,xlrd

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 26
android.ndk_api = 26
android.arch = arm64-v8a

android.enable_androidx = True
android.use_androidx = True
android.gradle_dependencies = androidx.documentfile:documentfile:1.0.1

p4a.branch = develop
