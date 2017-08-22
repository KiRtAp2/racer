from pygame.image import load as image
import maploader

background = image(maploader.get_background_image())
car1_, car2_ = maploader.get_player_images()
car1, car2 = image(car1_), image(car2_)