import pygame
from spritesheet import Spritesheet
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.12
        self.image = Spritesheet('spritesheet.png').parse_sprite('pinguino.png')
        self.rect = self.image.get_rect()
        self.position, self.velocity = pygame.math.Vector2(0,0), pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,self.gravity)

        self.walk_animation_delay = 8  # Retardo en milisegundos entre cada cambio de frame de la animación de caminar
        self.walk_animation_timer = 0    # Temporizador para controlar el retardo de la animación de caminar

        self.walk_animation_frames = []  # Almacenará los frames de la animación de caminar
        self.walk_animation_index = 0    # Índice actual de la animación de caminar

        self.walk_animation_frames.append(pygame.image.load("AnimacionesSpriteSheets/AnimacionPinguino/sprite_0.png"))
        self.walk_animation_frames.append(pygame.image.load("AnimacionesSpriteSheets/AnimacionPinguino/sprite_1.png"))
        self.walk_animation_frames.append(pygame.image.load("AnimacionesSpriteSheets/AnimacionPinguino/sprite_2.png"))
        self.walk_animation_frames.append(pygame.image.load("AnimacionesSpriteSheets/AnimacionPinguino/sprite_3.png"))


    def draw(self, display):
        if self.FACING_LEFT:
            display.blit(pygame.transform.flip(self.walk_animation_frames[self.walk_animation_index], True, False), (self.rect.x, self.rect.y))
        else:
            display.blit(self.walk_animation_frames[self.walk_animation_index], (self.rect.x, self.rect.y))
        

    def update(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)

        # Avanzar al siguiente frame de la animación de caminar
        if self.LEFT_KEY or self.RIGHT_KEY:
            self.walk_animation_timer += dt
        if self.walk_animation_timer >= self.walk_animation_delay:
            self.walk_animation_index = (self.walk_animation_index + 1) % len(self.walk_animation_frames)
            self.walk_animation_timer = 0
        if not self.LEFT_KEY and not self.RIGHT_KEY:
            self.walk_animation_index = 0
        

    def horizontal_movement(self,dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .6
        elif self.RIGHT_KEY:
            self.acceleration.x += .6
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt

        if self.velocity.x > 0:
            self.FACING_LEFT = False
        elif self.velocity.x < 0:
            self.FACING_LEFT = True

        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

        # Evitar que el jugador salga de la pantalla por el lado izquierdo
        if self.position.x <= 0:
            self.position.x = .2
            self.rect.x = self.position.x

    def vertical_movement(self,dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 10
            self.on_ground = False

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionsx(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.x > 0:  # Si choca a la derecha
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif self.velocity.x < 0:  # Si choca a la izquierda
                self.position.x = tile.rect.right
                self.rect.x = self.position.x

    def checkCollisionsy(self, tiles):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:  # Si choca con el piso
                self.on_ground = True
                self.is_jumping = False
                self.velocity.y = 0
                self.position.y = tile.rect.top
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:  # Si choca con el techo
                self.velocity.y = 0
                self.position.y = tile.rect.bottom + self.rect.h
                self.rect.bottom = self.position.y



###### CLASE BOLA ########
class Bola:
    def __init__(self, position, speed, player):
        self.position = position
        self.speed = speed
        self.radius = 5
        self.color = (255, 255, 255)
        self.player = player
        ######ENEMIGO######
        self.enemigos = []  # Lista de enemigos

        ########### InstaClick ##########
        self.lanzarBola=False
        self.ContadorBoolean=False
        self.xO , self.yO = self.position
        self.relativoX , self.relativoY = 0, 0
        self.x1 , self.y1 , self.x2 , self.y2 , self.x3 , self.y3 = 0, 0, 0, 0, 0, 0
        self.a , self.b , self.c = 0, 0, 0
        self.h , self.co , self.ca = 0, 0, 0
        self.A , self.B , self.C = 0, 0, 0
        self.Arad = 0

        ########### WhileClick ##########
        self.contadorBola = 0
        self.t , self.g = 0, 0
        self.xBola , self.yBola = 0 , 0
        self.colision = False

    def check_collisions(self, tiles):
        for tile in tiles:
            if pygame.Rect(self.xBola, self.yBola, self.radius * 2, self.radius * 2).colliderect(tile.rect):
                self.colision = True
                

    def update(self, dt, player_position, tiles):
        if self.player.FACING_LEFT:
            self.position = player_position + pygame.math.Vector2(0, -20)
        else:
            self.position = player_position + pygame.math.Vector2(40, -20)
        self.check_collisions(tiles)
        self.check_enemy_collision()

    def check_enemy_collision(self):
        for enemigo in self.enemigos:
            if not self.colision:
                if pygame.Rect(self.xBola, self.yBola, self.radius * 2, self.radius * 2).colliderect(enemigo.rect) and enemigo.vivo:
                    # Restablecer la posición original de la bola
                    self.xBola, self.yBola = self.xO, self.yO
                    self.t = 0
                    self.xBola = self.xO
                    self.yBola = self.yO
                    self.colision = False
                    self.ContadorBoolean=False
                    enemigo.hit_count +=1
                    break
    
    def throwClick(self):
        if(self.lanzarBola): #Lo que pase aca SOLO pasa en el instante en el que se da el click para la bola
            self.xO, self.yO = self.position
            self.relativoX, self.relativoY = pygame.mouse.get_pos()
            self.ContadorBoolean=True

            (self.x1, self.y1) = (self.relativoX, self.relativoY)
            (self.x2, self.y2) = (self.xO, self.yO)
            (self.x3, self.y3) = (self.x1, self.y2)

            self.a = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
            self.b = math.sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
            self.c = math.sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)

            if self.a > self.b and self.a > self.c:
                self.h = self.a
                self.co = self.b
                self.ca = self.c
            elif self.b > self.a and self.b > self.c:
                self.h = self.b
                self.co = self.a
                self.ca = self.c
            else:
                self.h = self.c
                self.co = self.a
                self.ca = self.b

            # Calcula los ángulos de la trayectoria
            self.A = math.degrees(math.atan(self.co/self.ca))
            self.B = math.degrees(math.atan(self.ca/self.co))
            self.C = 90
            self.Arad = math.radians(self.A) #Angulo A en radianes
        

            

    def throwSec(self):
        if(self.ContadorBoolean): #LO QUE PONGA ACA SE EJECUTA DURANTE MAS O MENOS 1 SEGUNDO
            
            self.contadorBola+=1
            self.t+=0.1
            self.vO=100
            self.g=5 

            #Decide si se lanza a la izquierda o derecha
            if(self.relativoX > self.xO):
                self.xBola = self.xO + (self.vO * math.cos(self.Arad) * self.t)
            elif(self.relativoX < self.xO):
                self.xBola = self.xO - (self.vO * math.cos(self.Arad) * self.t)
            
            #Decide si se lanza hacia arriba o abajo
            if(self.relativoY > self.yO):
                self.yBola = self.yO + (self.vO * (math.sin(self.Arad)) * self.t) + ((1/2) * self.g * (self.t*self.t))
            elif(self.relativoY < self.yO):
                self.yBola = self.yO - (self.vO * (math.sin(self.Arad)) * self.t) + ((1/2) * self.g * (self.t*self.t))
            
        else:
            self.xBola = self.xO
            self.yBola = self.yO
            self.t=0
            self.colision = False

    def draw(self, canvas):
        if not (self.colision):
            if(self.ContadorBoolean) and self.xBola>=0:
                pygame.draw.circle(canvas, self.color, (int(self.xBola), int(self.yBola)), self.radius)
            else:
                pygame.draw.circle(canvas, self.color, (int(self.position.x), int(self.position.y)), self.radius)


