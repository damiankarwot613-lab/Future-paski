[app]

title = PaskiFuture
package.name = paskifuture
package.domain = org.paskifuture

source.dir = .
source.include_exts = py,png,jpg,kv,json

version = 1.0

requirements = python3,kivy==2.3.0,openpyxl,xlrd

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 33.0.2

android.enable_androidx = True
android.use_androidx = True
android.gradle_dependencies = androidx.documentfile:documentfile:1.0.1

p4a.branch = develop
