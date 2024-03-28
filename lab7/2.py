import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("bomsk_mp3")

clock = pygame.time.Clock()

youngblood = 'week7/5 Seconds Of Summer - Youngblood.mp3'
bbini = 'RIIZE - Get A Guitar.mp3'
bornthisway = 'Lady Gaga – Judas.mp3'

pygame.mixer.music.load('5 Seconds Of Summer - Youngblood.mp3')
myList = [youngblood, bbini, bornthisway]
pygame.mixer.music.play(-1)

flPause = False
index = 0
run = True

while run:
    screen.fill('Purple')
    player = pygame.image.load('player.png')
    screen.blit(player, (20, 20))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(myList):
                    index = 0
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(myList)-1
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()

    clock.tick(20)