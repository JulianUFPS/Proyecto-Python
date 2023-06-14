from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola
from palancas import Palanca
import pygame 

################################# Cargar una ventana y un reloj interno #################################
SONIDOS_DIR= "sonidos" ###Se acomoda la ubicación del sonido a una variable.
pygame.init()
pygame.mixer.init()

def load_sound(name):
    return pygame.mixer.Sound(os.path.join(SONIDOS_DIR, f"{name}.wav"))

musicIniciPantalla = load_sound("inicio")
musicInicio = load_sound ("inicioBajo")
soundLanzarNieve = load_sound("lanzar-bola")
soundPalanca = load_sound("palanca")
musicEnemigo = load_sound ("bajo-1-enemigos")
soundPuerta = load_sound("puerta")

##Reproducir:Inicio
musicInicio.play(-1)





DISPLAY_W, DISPLAY_H = 1280, 640
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60

habitacionActual=1
################################# Cargar las imagenes y el spritesheet ###################################
spritesheet = Spritesheet('spritesheet.png')
player = Player()

#################################### Cargar el nivel  #######################################

map = TileMap('Niveles/Nivel1-1.csv', spritesheet )
mapa1 = TileMap('Niveles/Nivel1-1.csv', spritesheet )
mapa2 = TileMap('Niveles/Nivel1-2TML.csv', spritesheet )
mapa3 = TileMap('Niveles/Nivel1-3TML.csv', spritesheet )

player.position.x, player.position.y = map.start_x, map.start_y
player.bola = Bola(player.position, player.velocity, player)

######### NIVEL 1 #######
#Fase 1:
palanca1 = Palanca(1150, 192, 66, 66)
#Fase 2:
palanca2 = Palanca(1152, 320, 64, 64)
palanca3 = Palanca(576, 64, 64, 64)
#Fase 3:
palanca4 = Palanca(1216, 512, 64, 64)
palanca5 = Palanca(1024, 192, 64, 64)
palanca6 = Palanca(1216, 192, 64, 64)

################################# GAME LOOP ##########################

while running:
    dt = clock.tick(120) * 0.001 * TARGET_FPS
    ################################# Checar el input #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               player.LEFT_KEY, player.FACING_LEFT = True, True
            elif event.key == pygame.K_d:
                player.RIGHT_KEY, player.FACING_LEFT = True, False
            elif event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.LEFT_KEY = False
            elif event.key == pygame.K_d:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False
        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        player.bola.lanzarBola = True
        player.bola.throwClick()
        ##sound
        soundLanzarNieve.play()


    player.bola.throwSec()

    if(player.bola.contadorBola>=100) or (player.bola.colision):
        player.bola.ContadorBoolean=False
        player.bola.contadorBola=0
         
    player.bola.lanzarBola = False

    ########### CAMBIAR DE HABITACION ####################
    
    if player.position.x>=1216:
        habitacionActual+=1
        if habitacionActual==2:
            player.position.x = 64
            player.position.y = 576
        elif habitacionActual==3:
            player.position.x = 64
            player.position.y = 576
    
    if habitacionActual==1:
        map = mapa1
    elif habitacionActual==2:
        map = mapa2
    elif habitacionActual==3:
        map = mapa3
        
    ########### DETECTAR CAMBIOS DE PALANCA ##############
    if palanca1.detect_collision(player.bola) and habitacionActual==1:
        mapa1 = TileMap('Niveles/Nivel1-1CLEAN.csv', spritesheet )
        #sonidos: 
        soundPalanca.play()
        soundPuerta.play()

    if palanca2.detect_collision(player.bola) and habitacionActual==2:
        mapa2 = TileMap('Niveles/Nivel1-2TMLCLEAN1.csv', spritesheet )
         ##sonidos
        soundPalanca.play()
        soundPuerta.play()   
    if palanca3.detect_collision(player.bola) and habitacionActual==2:
        mapa2 = TileMap('Niveles/Nivel1-2TMLCLEAN2.csv', spritesheet )
        ##sonidos:
        soundPalanca.play()
        soundPuerta.play()

    if palanca4.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN1.csv', spritesheet )
        ##sonidos:
        soundPalanca.play()
        soundPuerta.play() 
    
    if palanca5.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN2.csv', spritesheet )
        ##sonidos: 
        soundPalanca.play()
        soundPuerta.play()
    
    if palanca6.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN3.csv', spritesheet )
        ##sonidos: 
        soundPalanca.play()
        soundPuerta.play()

        
    ################################# Actualizar / Animar Sprites #################################

    if(player.bola.relativoX>player.position.x):
        player.FACING_LEFT = False
    elif(player.bola.relativoX<player.position.x):
        player.FACING_LEFT = True

    player.update(dt, map.tiles)
    player.bola.update(dt, player.position, map.tiles)

    ################################# Actualizar ventana #################################

    canvas.fill((0, 180, 240)) # Llena la ventana de azul
    map.draw_map(canvas)

    player.draw(canvas)
    player.bola.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.update()

    