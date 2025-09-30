import pygame


pygame.init()
dis=pygame.display.set_mode((1000, 800))
dis_over=False
x = 10
y = 10
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    while x < 1000:
        color = 255, 145, 12
        pygame.draw.rect(dis, color, (x, 10, 40, 40), 3)
        x += 50
    while y < 800:
        color = 255, 145, 12
        pygame.draw.rect(dis, color, (x, y, 40, 40), 3)
        y += 50
        numbers = font.render(f"{x}{y}", True, 
    pygame.display.update()
quit()