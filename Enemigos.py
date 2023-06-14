import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("Imagenes/enemy.png").convert_alpha()
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.hit_count = 0
        self.opacidad = 300
        
        
        self.vivo=False
        self.murio=False

    def draw(self, display):
        self.image.set_alpha(self.opacidad)
        display.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.rect.x, self.rect.y))

    def check_collision(self, bola):
        if self.hit_count < 3 and self.vivo:
            if pygame.Rect(bola.xBola, bola.yBola, bola.radius * 2, bola.radius * 2).colliderect(self.rect) and self.vivo:
                
                self.hit_count += 1
                if self.hit_count == 3:
                    self.image = pygame.image.load("Imagenes/enemy.png").convert_alpha() #Pasa a ser una imagen literalmente transparente, sin nada en ella.
                    self.murio=True

    def update(self):
        if self.murio:
            self.opacidad -=4
            self.rect.y -=8
            self.height +=4
            self.vivo=False
        if self.rect.y<= -1000:
            self.murio=False
        
