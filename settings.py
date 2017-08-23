import json

settings_file = open("settings.json", encoding="utf-8")

settings = json.load(settings_file)

window_width = settings["window-width"]
window_height = settings["window-height"]

framerate = settings["framerate"]

map_file = settings["map-file"]

map_version = settings["current-map-version"]

debug = settings["debug"]