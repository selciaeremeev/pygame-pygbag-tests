# coding: utf-8
import sys
import asyncio

import pygame


async def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("pygame-pygbag-tests")
    clock = pygame.time.Clock()

    x, y = 100, 100

    while True:
        screen.fill((255, 255, 255))
        screen.blit(pygame.font.Font(None, 30).render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0)), [0, 0])
        screen.blit(pygame.font.Font(None, 30).render("TEST", True, (0, 0, 0)), [x, y])
        pygame.display.update()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            x -= 1
        if pressed[pygame.K_RIGHT]:
            x += 1
        if pressed[pygame.K_UP]:
            y -= 1
        if pressed[pygame.K_DOWN]:
            y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
