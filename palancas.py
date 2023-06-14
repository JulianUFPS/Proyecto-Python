import pygame
import math
from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola

class Palanca:
    def __init__(self, x, y, width, height, canvas, habitacionActual):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.animation_delay = 5
        self.animation_timer = 0
        self.animation_frames = []
        self.animation_index = 0
        self.colisiono = False
        self.habitacionActual = habitacionActual

        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_0.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_1.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_2.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_3.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_4.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_5.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_6.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_7.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_8.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_9.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_10.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_11.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_12.png"), (64, 64)))
        self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Palanca/sprite_13.png"), (64, 64)))

    
    def play_animation(self):    
        self.animation_timer += 1
        if self.animation_timer >= self.animation_delay:
            self.animation_timer = 0
            self.animation_index += 1
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 13
        current_frame = self.animation_frames[self.animation_index]
        # Dibujar el marco de animación en las coordenadas de la palanca
        self.canvas.blit(current_frame, (self.x, self.y))
    
    def llamarAnimaciones(self):
        if self.colisiono:
            self.play_animation()
            

    
    def detect_collision(self, bola):
        bola_rect = pygame.Rect(bola.xBola, bola.yBola, bola.radius * 1, bola.radius * 1)
        palanca_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if bola_rect.colliderect(palanca_rect):
            # Ejecutar la animación en las coordenadas de la palanca
            
            return True
        return False
    
    