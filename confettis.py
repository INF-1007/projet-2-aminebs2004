import random
import pygame
from config import WIDTH, HEIGHT
class Confetti:
    def __init__(self):
        self.x = random.randint(-200,WIDTH)
        self.y = random.randint(-200,HEIGHT)
        self.speed = (1,10)
        self.size = random.randint(7, 12)
        self.color = (random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
    
    def mettre_à_jour(self):
        self.y += self.speed[1]
        self.x += self.speed[0]
        if self.y > HEIGHT:
            self.y = random.randint(-200,HEIGHT)
            self.x = random.randint(-200, WIDTH)


    def dessiner (self,surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 10, 12))

