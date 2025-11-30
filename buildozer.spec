[app]

# Tətbiq haqqında məlumat
title = Snakeibo Mobile
package.name = snakeibo
package.domain = com.rex.snakeibo
version = 1.0.2

# Əsas Python faylını göstəririk
main.py = snakeibo_new.py

# Bütün faylların yerləşdiyi qovluq (səs faylları artıq buradadır!)
source.dir = .

# Tələb olunan modullar (AdMob Geri Qayıtdı)
requirements = python3,kivy,kivy-admob==0.1.0

# Qalan App parametrləri
icon.filename = %(source.dir)s/icon.png
fullscreen = 1
orientation = portrait 

[build]
# Android SDK parametrləri
android.accept_sdk_license = True
android.minapi = 21
android.api = 33
android.no_obfuscate = 1

# İcazələr
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Reklam və asılılıqlar (AdMob Geri Qayıtdı)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:23.0.0'

[packaging]
android.release = True

[buildozer]
log_level = 2
warn_on_root = 1
