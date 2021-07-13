import pygame
import random
import sys
from pygame.locals import QUIT

pygame.init()
screen_info = pygame.display.Info()
width = screen_info.current_w
height = screen_info.current_h
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fish_image = pygame.image.load('fish.png')
fish_image = pygame.transform.smoothscale(fish_image, (80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width // 2, height // 2)
speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180 - rotation)

def move_fish():
  global fish_image
  info_now = pygame.display.Info()
  fish_rect.move_ip(speed)
  if fish_rect.left < 0 or fish_rect.right > info_now.current_w:
    speed[0] = speed[0] * -1 
    fish_image = pygame.transform.flip(fish_image, True, False)
    fish_rect.move_ip(speed[0], 0)
  if fish_rect.top < 0 or fish_rect.bottom > info_now.current_h:
    speed[1] = speed[1] * -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1])

print('')
print('F I S H')
print(' ')

def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    move_fish()
    screen.fill((40, 180, 255))
    screen.blit(fish_image, fish_rect)
    pygame.display.update()

if __name__ == '__main__':
  main()