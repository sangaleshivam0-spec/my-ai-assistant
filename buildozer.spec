[app]

title = My AI Assistant
package.name = myaiassistant
package.domain = org.myassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,google-genai

orientation = portrait

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

[buildozer:android]

android.accept_sdk_license = True
