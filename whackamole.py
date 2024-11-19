import pygame
import random
#change

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        def positions():
            return random.randrange(0, 640 // 32) * 32, random.randrange(0, 512 // 32) * 32
        position = (0, 0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickx, clicky = event.pos
                    sigma = pygame.Rect(position[0], position[1], 32, 32)
                    if sigma.collidepoint(clickx, clicky):
                        position = positions()
            screen.fill("yellow")
            for i in range(0, 640, 32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
            for j in range(0, 512, 32):
                pygame.draw.line(screen, (0, 0, 0), (0, j), (640, j))
            screen.blit(mole_image, mole_image.get_rect(topleft=position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
