import sys

import pygame

import settings
import json
from utils import supported

selected_map = settings.map_file

map_file = open(selected_map, "r", encoding="utf-8")

map_info = json.load(map_file)

if not pygame.font.get_init():
    pygame.font.init()

map_font = pygame.font.SysFont(map_info["font-name"], 70)

if not supported(map_info["map-version"]):
    print("MAP INCOMPATIBLE")
    sys.exit(-1)

def get_background_image():
    return map_info["mapimage"]

def get_player_images():
    return (map_info["player1"]["carimage"], map_info["player2"]["carimage"])

def get_player_info(num):
    return (map_info["player"+str(num)]["spawnlocation"], map_info["player"+str(num)]["size"])

def get_player_velocity():
    return map_info["player-velocity"]

def get_starting_orientation():
    return map_info["starting-orientation"]

def get_rotation_speed():
    return map_info["rotation-speed"]

def get_font():
    return map_font

def valid_position(x, y, sx, sy):
    valid = False
    for l in map_info["trajectory"]:
        if l[0] < x and x+sx < l[0]+l[2]:
            if l[1] < y and y+sy < l[1]+l[3]:
                valid = True
    return valid