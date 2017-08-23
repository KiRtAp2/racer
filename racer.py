import pygame

import colors
import maploader
import player
import settings
from sys import exit as quit

import texture

pygame.init()

window = pygame.display.set_mode((settings.window_width, settings.window_height))

clock = pygame.time.Clock()

car1 = player.Player(*maploader.get_player_info(1), texture.car1)
car2 = player.Player(*maploader.get_player_info(2), texture.car2)

def main():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    car1.rotate(1)
                if event.key == pygame.K_LEFT:
                    car1.rotate(-1)

                if event.key == pygame.K_a:
                    car2.rotate(-1)
                if event.key == pygame.K_d:
                    car2.rotate(1)

                # if event.key == pygame.K_f and settings.debug:
                #     pygame.

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    car1.stop_rotating()
                elif event.key in (pygame.K_a, pygame.K_d):
                    car2.stop_rotating()

        window.blit(texture.background, (0,0))
        car1.tick(window)
        car2.tick(window)
        pygame.display.update()

        clock.tick(settings.framerate)

def menu():
    while True:

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                quit()

            if event.type==pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    main()

        window.fill(colors.white)
        pygame.display.update()



if __name__ == '__main__':
    menu()