"""import pygame
import random
pygame.init()
dis=pygame.display.set_mode((1000, 800))
class Snowlake:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(-50, 0)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > 400:
            self.x = random.randint(0, 500)
            self.y = random.randint(-50, 0)
            self.speed = random.uniform(1, 3)
            
dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            print(event)
            pygame.quit()
    color1 = 255, 255, 255
    color2 = 0, 0, 0
    color3 = 255, 255, 255
    color4 = 210, 105, 30
    pygame.draw.circle(dis,color1, [500, 200], 75, 0)
    pygame.draw.circle(dis, color2, [470, 180], 12, 0)
    pygame.draw.circle(dis, color3, [470, 175], 4, 0)
    pygame.draw.circle(dis, color3, [468, 180], 3, 0)
    pygame.draw.circle(dis, color2, [530, 180], 12, 0)
    pygame.draw.circle(dis, color3, [530, 174], 4, 0)
    pygame.draw.circle(dis, color3, [530, 180], 3, 0)
    pygame.draw.circle(dis, color1, [500, 325], 100, 0)
    pygame.draw.circle(dis,color2, [500, 325], 5, 0)
    pygame.draw.circle(dis,color2, [500, 345], 5, 0)

    pygame.draw.circle(dis, color1, [500, 450], 120, 0)
    pygame.draw.polygon(dis,[210, 105, 30], [(500, 190), (500, 210), (560, 200)])


    pygame.display.update()"""


