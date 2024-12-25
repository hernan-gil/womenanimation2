import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation with Combined Backgrounds")

# Cargar las imágenes
sprite_sheet = pygame.image.load("sprites/Acrobat Female Base - Yoyo[MZMV].png").convert_alpha()
background_image0 = pygame.image.load("background/sky.png").convert()
background_image = pygame.image.load("background/middle-mountains.png").convert_alpha()

# Redimensionar el fondo al tamaño de la pantalla
background_image0 = pygame.transform.scale(background_image0, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Tamaño de cada subimagen
SPRITE_WIDTH = 1440 // 9  # Dividir el ancho total entre 9 columnas
SPRITE_HEIGHT = 960 // 6  # Dividir el alto total entre 6 filas

# Configuración de la animación
FPS = 10  # Cuadros por segundo
clock = pygame.time.Clock()

# Crear una lista para almacenar cada subimagen del sprite
frames = []

for row in range(6):  # 6 filas
    for col in range(9):  # 9 columnas
        x = col * SPRITE_WIDTH
        y = row * SPRITE_HEIGHT
        frame = sprite_sheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
        frames.append(frame)

# Animar desde el primer cuadro al último
frame_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el fondo base
    background_image0.set_alpha(128)  # Ajusta el nivel de transparencia (0 a 255)
    screen.blit(background_image0, (0, 0))

    # Crear una nueva superficie con transparencia para combinar los fondos
    blended_background = background_image.copy()
    #blended_background.set_alpha(128)  # Ajusta el nivel de transparencia (0 a 255)
    screen.blit(blended_background, (0, 0))

    # Dibujar el cuadro actual
    screen.blit(frames[frame_index], (SCREEN_WIDTH // 2 - SPRITE_WIDTH // 2, SCREEN_HEIGHT // 2 - SPRITE_HEIGHT // 2))
    pygame.display.flip()

    # Avanzar al siguiente cuadro
    frame_index = (frame_index + 1) % len(frames)

    # Controlar la velocidad de la animación
    clock.tick(FPS)

# Salir del programa
pygame.quit()
sys.exit()
