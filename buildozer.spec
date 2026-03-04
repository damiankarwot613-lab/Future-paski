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

android.sdk = 24
android.ndk = 25b
android.api = 33
android.ndk_api = 21

android.enable_androidx = True
android.use_androidx = True
android.gradle_dependencies = androidx.documentfile:documentfile:1.0.1
