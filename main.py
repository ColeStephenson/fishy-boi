import pygame
import random
import sys
from pygame.locals import QUIT

pygame.init()
screen_info = pygame.display.Info()
width = screen_info.current_w
height = screen_info.current_h
size = (width, height)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
dvd_image = pygame.image.load('dvdlogored.png')
dvd_image = pygame.transform.smoothscale(dvd_image, (80, 80))
dvd_rect = dvd_image.get_rect()
dvd_rect.center = (width // 2, height // 2)
speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
# dvd_image = pygame.transform.rotate(dvd_image, 180 - rotation)

def change_pic():
  global dvd_image
  ranpic = random.randint (0, 6)
  if ranpic == 1:
    dvd_image = pygame.image.load('dvdlogored.png')
  elif ranpic == 2:
    dvd_image = pygame.image.load('dvdlogoorange.png')
  elif ranpic == 3:
    dvd_image = pygame.image.load('dvdlogoyellow.png')
  elif ranpic == 4:
    dvd_image = pygame.image.load('dvdlogogreen.png')
  elif ranpic == 5:
    dvd_image = pygame.image.load('dvdlogoblue.png')
  elif ranpic == 6:
    dvd_image = pygame.image.load('dvdlogopurple.png')
  dvd_image = pygame.transform.smoothscale(dvd_image, (80, 80))
  dvd_rect = dvd_image.get_rect()
  dvd_rect.center = (width // 2, height // 2)

def move_dvd():
  global dvd_image
  info_now = pygame.display.Info()
  dvd_rect.move_ip(speed)
  if dvd_rect.left < 0 or dvd_rect.right > info_now.current_w:
    speed[0] = speed[0] * -1 
    change_pic()
    # dvd_image = pygame.transform.flip(dvd_image, True, False)
    dvd_rect.move_ip(speed[0], 0)
  if dvd_rect.top < 0 or dvd_rect.bottom > info_now.current_h:
    speed[1] = speed[1] * -1
    change_pic()
    # dvd_image = pygame.transform.flip(dvd_image, False, True)
    dvd_rect.move_ip(0, speed[1])

print('')
print('D V D')
print(' ')

def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    move_dvd()
    screen.fill((0, 0, 0))
    screen.blit(dvd_image, dvd_rect)
    pygame.display.update()

if __name__ == '__main__':
  main()