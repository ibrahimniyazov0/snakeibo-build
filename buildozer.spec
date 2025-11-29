[app]
title = Snakeibo Mobile
package.name = snakeibo
package.domain = com.rex.snakeibo
version = 1.0.2
main.py = snakeibo_new.py
icon.filename = %(source.dir)s/icon.png
# source.dir səhvini düzəltdik. Default olaraq cari qovluğu göstərir.
source.dir = .
requirements = python3,kivy,kivy-admob==0.1.0
# "all" dəyərini sildik. Default dəyəri istifadə edirik (və ya 'portrait' yazmaq olar).
# orientation = all # Silindi. Default olaraq avtomatik dönmə aktivdir.
fullscreen = 1

[build]
android.accept_sdk_license = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:23.0.0'
android.minapi = 21
android.api = 33
android.no_obfuscate = 1
export_orientation = False

[packaging]
android.release = True

[buildozer]
log_level = 2
warn_on_root = 1
