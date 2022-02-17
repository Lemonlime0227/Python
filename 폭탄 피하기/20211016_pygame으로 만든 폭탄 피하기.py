#pygame으로 만든 폭탄피하기
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
#pygame.key.set_repeat(1,1)

large_font = pygame.font.SysFont("malgungothic", 72)
small_font = pygame.font.SysFont("malgungothic", 40)
score = 0
game_over = False

bomb_image = pygame.image.load('bomb.png')
#bomb = bomb_image.get_rect(left = 100, top =100)
bombs = []
for i in range(5):
#    bomb = bomb_image.get_rect(left=(i+1) * 100, top = (i+1) * 100)
    bomb = bomb_image.get_rect(left = random.randint(0,600), top = - 100)
    bombs.append(bomb)
circle_image = pygame.image.load('circle1.png')
circle = circle_image.get_rect()
circle.left = 300 - circle_image.get_width() // 2
circle.top = 800 - circle_image.get_height()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
game_over_sound = pygame.mixer.Sound('game_over.wav')

while True:
    screen.fill((182,182,182))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN and not game_over:
        if event.key == pygame.K_LEFT:
            circle.left -= 20
        elif event.key == pygame.K_RIGHT:
            circle.left += 20
        elif event.key == pygame.K_UP:
            circle.top -= 20
        elif event.key == pygame.K_DOWN:
            circle.top += 20
    if not game_over:
        for bomb in bombs:
            bomb.top += 5
            if bomb.top > 800:
                #bomb.left = random.randint(0,600-bomb.width)
                #bomb.top = -100
                bombs.remove(bomb)
                bomb = bomb_image.get_rect(left = random.randint(0,600 - bomb.width), top = -100)
                bombs.append(bomb)
                score += 10
        
        if circle.left < 0:
            circle.left = 0
        elif circle.right > 600:
            circle.right = 600

        for bomb in bombs:
            if bomb.colliderect(circle):
                game_over = True
                pygame.mixer.music.stop()
                game_over_sound.play()
    
    #screen.blit(circle_image , (300 - circle_image.get_width()//2 , 800 - circle_image.get_height()))
    screen.blit(circle_image, circle)
    #screen.blit(bomb_image, bomb)
    for bomb in bombs:
        screen.blit(bomb_image,bomb)

    score_image = small_font.render("점수 {}".format(score), True, (255, 255, 0))
    screen.blit(score_image, (10,10))


    if game_over:
        game_over_image = large_font.render('게임 종료', True, (255, 0, 0))
        #screen.blit(game_over_image, (300, 400))
        screen.blit(game_over_image, (300 - game_over_image.get_width() // 2 , 400 - game_over_image.get_height() // 2))
        
        
    pygame.display.update()
    clock.tick(30)
pygame.quit()

