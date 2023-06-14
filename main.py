from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola
from palancas import Palanca
from puertas import Puerta
from Enemigos import Enemigo
################################# Cargar una ventana y un reloj interno #################################
SONIDOS_DIR= "sonidos" ###Se acomoda la ubicación del sonido a una variable.
pygame.init()
pygame.mixer.init()

def load_sound(name):
    return pygame.mixer.Sound(os.path.join(SONIDOS_DIR, f"{name}.wav"))
def load_soundmp3(name):
    return pygame.mixer.Sound(os.path.join(SONIDOS_DIR, f"{name}.ogg"))

musicIniciPantalla = load_sound("inicio")
musicInicio = load_soundmp3 ("inicioBajo")
soundLanzarNieve = load_sound("lanzar-bola")
soundPalanca = load_sound("palanca")
musicEnemigo = load_sound ("bajo-1-enemigos")
soundPuerta = load_sound("puerta")

#Reproducir:Inicio
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


fondo = pygame.image.load("AnimacionesSpriteSheets/Fondos/FondoAfuera/fondo_00.png").convert()
fondoFabrica= pygame.image.load("AnimacionesSpriteSheets/Fondos/FondoFabrica-1.png").convert()
fondoFabrica2 = pygame.image.load("AnimacionesSpriteSheets/Fondos/FondoFabrica2-1.png").convert()
fondoRedimensionado = pygame.transform.scale(fondo, (DISPLAY_W, DISPLAY_H))
fondoFabricaRedimensionado = pygame.transform.scale(fondoFabrica, (DISPLAY_W, DISPLAY_H))
fondoFabrica2Redimensionado = pygame.transform.scale(fondoFabrica2, (DISPLAY_W, DISPLAY_H))
fondoFinal = pygame.image.load("AnimacionesSpriteSheets/Fondos/FondoAfuera/fondo_00.png").convert()

enemigos = []
enemigo1= Enemigo(896, 384, 128, 192)

enemigos.append(enemigo1)
enemigo2= Enemigo(640, 256, 128, 192)

enemigos.append(enemigo2)
enemigo3 = Enemigo(1152, 256, 128, 192)

enemigos.append(enemigo3)


#################################### Cargar el nivel  #######################################

map = TileMap('Niveles/Nivel1-1.csv', spritesheet )
mapa1 = TileMap('Niveles/Nivel1-1.csv', spritesheet )
mapa2 = TileMap('Niveles/Nivel1-2TML.csv', spritesheet )
mapa3 = TileMap('Niveles/Nivel1-3TML.csv', spritesheet )

player.position.x, player.position.y = map.start_x, map.start_y
player.bola = Bola(player.position, player.velocity, player)
player.bola.enemigos = enemigos
######### NIVEL 1 #######
#Fase 1:
palanca1 = Palanca(1152, 192, 64, 64, canvas, habitacionActual)
puerta1 = Puerta(1216, 448, 64, 128, canvas, habitacionActual, False)
#Fase 2:
palanca2 = Palanca(1152, 320, 64, 64, canvas, habitacionActual)
palanca3 = Palanca(576, 64, 64, 64, canvas, habitacionActual)
puerta2 = Puerta(512, 128, 128, 64, canvas, habitacionActual, True)
puerta3 = Puerta(1216, 448, 64, 128, canvas, habitacionActual, False)
#Fase 3:
palanca4 = Palanca(1216, 512, 64, 64, canvas, habitacionActual)
palanca5 = Palanca(1024, 192, 64, 64, canvas, habitacionActual)
palanca6 = Palanca(1216, 192, 64, 64, canvas, habitacionActual)
puerta4 = Puerta(768, 448, 128, 64, canvas, habitacionActual, True)
puerta5 = Puerta(1088, 320, 64, 128, canvas, habitacionActual, False)
puerta6 = Puerta(1216, 0, 64, 128, canvas, habitacionActual, False)


################################# GAME LOOP ##########################

while running:
    dt = clock.tick(120) * 0.001 * TARGET_FPS
    current_time = pygame.time.get_ticks()
    
    ################################# Actualizar ventana #################################
    ######### CAMBIAR DE FONDO ###########
    if habitacionActual == 1:
        fondoFinal = fondoRedimensionado
    elif habitacionActual == 2:
        fondoFinal = fondoFabricaRedimensionado
        
    elif habitacionActual == 3:
        fondoFinal = fondoFabrica2Redimensionado
    canvas.blit(fondoFinal, [0, 0])

    map.draw_map(canvas)

    player.draw(canvas)
    player.bola.draw(canvas)
    
    
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
        
   
        enemigo1.vivo=True
        enemigo1.draw(canvas)
        enemigo1.update()
        enemigo1.check_collision(player.bola)

       
        enemigo2.vivo=True
        enemigo2.draw(canvas)
        enemigo2.update()
        enemigo2.check_collision(player.bola)

    elif habitacionActual==3:
        map = mapa3

        enemigo3.vivo=True
        enemigo3.draw(canvas)
        enemigo3.update()
        enemigo3.check_collision(player.bola)
    
    
    if habitacionActual==1:
        palanca1.llamarAnimaciones()
        puerta1.llamarAnimaciones()
    if habitacionActual==2:
        palanca2.llamarAnimaciones()
        palanca3.llamarAnimaciones()
        puerta2.llamarAnimaciones()
        puerta3.llamarAnimaciones()
    if habitacionActual==3:
        palanca4.llamarAnimaciones()
        palanca5.llamarAnimaciones()
        palanca6.llamarAnimaciones()
        puerta4.llamarAnimaciones()
        puerta5.llamarAnimaciones()
        puerta6.llamarAnimaciones()

 
    
    ########### DETECTAR CAMBIOS DE PALANCA ##############
    if palanca1.detect_collision(player.bola) and habitacionActual==1:
        mapa1 = TileMap('Niveles/Nivel1-1CLEAN.csv', spritesheet )
        palanca1.colisiono=True
        puerta1.activada=True
        #sonidos: 
        soundPalanca.play()
        soundPuerta.play()

    if palanca2.detect_collision(player.bola) and habitacionActual==2:
        mapa2 = TileMap('Niveles/Nivel1-2TMLCLEAN1.csv', spritesheet )
        palanca2.colisiono=True
        puerta2.activada=True
        ##sonidos
        soundPalanca.play()
        soundPuerta.play() 
        
    if palanca3.detect_collision(player.bola) and habitacionActual==2:
        mapa2 = TileMap('Niveles/Nivel1-2TMLCLEAN2.csv', spritesheet )
        palanca3.colisiono=True
        puerta3.activada=True
        ##sonidos:
        soundPalanca.play()
        soundPuerta.play()

    if palanca4.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN1.csv', spritesheet )
        palanca4.colisiono=True
        puerta4.activada=True
        ##sonidos:
        soundPalanca.play()
        soundPuerta.play() 
        
    if palanca5.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN2.csv', spritesheet )
        palanca5.colisiono=True
        puerta5.activada=True
        ##sonidos: 
        soundPalanca.play()
        soundPuerta.play()
    
    if palanca6.detect_collision(player.bola) and habitacionActual==3:
        mapa3 = TileMap('Niveles/Nivel1-3TMLCLEAN3.csv', spritesheet )
        palanca6.colisiono=True
        puerta6.activada=True
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

    window.blit(canvas, (0,0))
    pygame.display.update()

    