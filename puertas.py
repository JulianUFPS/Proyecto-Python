import pygame
import math
from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola

class Puerta:
    def __init__(self, x, y, width, height, canvas, habitacionActual, girada):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.animation_delay = 4
        self.animation_timer = 0
        self.animation_frames = []
        self.animation_index = 0
        self.activada = False
        self.animacionAcabada = False
        self.habitacionActual = habitacionActual
        self.girada = girada
        
        
        if not self.girada:
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_00.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_01.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_02.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_03.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_04.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_05.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_06.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_07.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_08.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_09.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_10.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_11.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_12.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_13.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_14.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_15.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_16.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_17.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_18.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_19.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_20.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_21.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_22.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/puerta_23.png"), (self.width, self.height)))

        elif self.girada:
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_00.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_01.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_02.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_03.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_04.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_05.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_06.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_07.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_08.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_09.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_10.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_11.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_12.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_13.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_14.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_15.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_16.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_17.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_18.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_19.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_20.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_21.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_22.png"), (self.width, self.height)))
            self.animation_frames.append(pygame.transform.scale(pygame.image.load("AnimacionesSpriteSheets/Puerta/Volteada/puerta_23.png"), (self.width, self.height)))


        
    def play_animation(self):    
        self.animation_timer += 1
        if self.animation_timer >= self.animation_delay:
            self.animation_timer = 0
            self.animation_index += 1
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 23
                self.animacionAcabada=True
        current_frame = self.animation_frames[self.animation_index]
        # Dibujar el marco de animación en las coordenadas de la puerta
        self.canvas.blit(current_frame, (self.x, self.y))
    
    def llamarAnimaciones(self):
        if self.activada and not self.animacionAcabada:
            self.play_animation()