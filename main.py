import pygame

pygame.init()
screen_info = pygame.display.Info()
size = (screen_info.current_w, screen_info.current_h)    # tuple
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fish_image = pygame.image.load('think_fish.png')

def main():
  while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()

# print(' ')
# print('F I S H')
# print(' ')