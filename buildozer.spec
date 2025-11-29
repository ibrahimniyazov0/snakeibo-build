[app]
title = Snakeibo Mobile
package.name = snakeibo
package.domain = com.rex.snakeibo
version = 1.0.1
main.py = snakeibo_new.py
icon.filename = %(source.dir)s/icon.png
requirements = python3,kivy,kivy-admob==0.1.0
orientation = all
android.minapi = 21
android.api = 33
android.no_obfuscate = 1

[build]
android.accept_sdk_license = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE
# AdMob APP ID SİZİN ÜÇÜN: ca-app-pub-6525217937280813~1393662594
android.extra_manifest_xml = <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="ca-app-pub-6525217937280813~1393662594"/>
export_orientation = False

[packaging]
android.release = True
