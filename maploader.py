import sys
import settings
import json
from utils import supported

selected_map = settings.map_file

map_file = open(selected_map, "r", encoding="utf-8")

map_info = json.load(map_file)

if not supported(map_info["map-version"]):
    print("MAP INCOMPATIBLE")
    sys.exit(-1)

def get_background_image():
    return map_info["mapimage"]

def get_player_images():
    return (map_info["player1"]["carimage"], map_info["player2"]["carimage"])

def get_player_info(num):
    return (map_info["player"+str(num)]["spawnlocation"], map_info["player"+str(num)]["size"])