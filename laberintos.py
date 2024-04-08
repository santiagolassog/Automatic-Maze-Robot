"""------------------------------------------------
Created on Mon Apr  8 09:01:42 2024
@author: Santiago Lasso
------------------------------------------------"""
import numpy as np
import pygame
from pygame.locals import *
from collections import deque

# Configuración tamaño de ventana
WIDTH, HEIGHT = 500, 500
MOVE_ROBOT_EVENT = pygame.USEREVENT + 1

# Velocidad de movimiento del robot
vel = 250

# Inicializar Pygame
pygame.init()

# Crear ventana y título
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Laberintos Automático")

# Cargar imágenes
pared = pygame.image.load('Images/wall.png')
suelo = pygame.image.load('Images/floor.png')
robot = pygame.image.load('Images/car_der.png')
robot_left = pygame.image.load('Images/car_izq.png')
out1 = pygame.image.load('Images/out1.png') 
fin_bg = pygame.image.load('Images/bg_delivered.png') 

# Escalar imágenes
pared = pygame.transform.scale(pared, (50, 50))
suelo = pygame.transform.scale(suelo, (50, 50))
robot = pygame.transform.scale(robot, (50, 50))
robot_left = pygame.transform.scale(robot_left, (50, 50))
out1 = pygame.transform.scale(out1, (50, 50))
fin_bg = pygame.transform.scale(fin_bg, (WIDTH, HEIGHT))

# Mapa y posición inicial del robot
columnas, filas = 10, 10
pos_x, pos_y = 0, 0
direccion = 'derecha'

coordenadas = (9, 9)
mapa = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])

# coordenadas = (0, 6)
# mapa = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#                   [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#                   [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#                   [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

# coordenadas = (6, 6)
# mapa = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#                   [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#                   [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#                   [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

# coordenadas = (8, 0)
# mapa = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#                   [0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
#                   [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#                   [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
#                   [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

salida_x, salida_y = coordenadas

# Función para encontrar la ruta hacia la salida utilizando BFS
def find_path_bfs():
    global pos_x, pos_y, fin, direccion

    # Inicializar matrices para rastrear las celdas visitadas y sus padres
    visited = np.zeros((filas, columnas), dtype=bool)
    parent = np.empty((filas, columnas, 2), dtype=int)

    # Definir las direcciones posibles de movimiento: arriba, abajo, izquierda, derecha
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Inicializar una cola para el BFS, comenzando desde la posición inicial del robot
    queue = deque([(pos_x, pos_y)])

    while queue:
        # Extraer la posición actual de la cola
        x, y = queue.popleft()
        visited[y, x] = True

        # Verificar si la posición actual es la salida del laberinto
        if (x, y) == (salida_x, salida_y):
            
            # Reconstruir el camino desde la salida hasta la posición inicial
            path = [(x, y)]
            while (x, y) != (pos_x, pos_y):
                x, y = parent[y, x]
                path.append((x, y))
            path.reverse()

            # Recorrer el camino y actualizar la dirección del robot
            for x, y in path[1:]:
                if x < pos_x:
                    direccion = 'izquierda'
                elif x > pos_x:
                    direccion = 'derecha'
                elif y < pos_y:
                    direccion = 'arriba'
                elif y > pos_y:
                    direccion = 'abajo'
                pos_x, pos_y = x, y
                
                # Retraso para visualizar el movimiento
                pygame.time.delay(vel)
                map_draw()
                pygame.display.flip()

            # Marcar que el juego ha terminado
            fin = True
            break

        # Explorar las celdas adyacentes
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Verificar si la celda adyacente es válida para moverse
            if 0 <= new_x < columnas and 0 <= new_y < filas and not visited[new_y, new_x] and mapa[new_y, new_x] == 0:
                # Registrar la posición padre de la celda adyacente y agregarla a la cola para su exploración
                parent[new_y, new_x] = (x, y)
                queue.append((new_x, new_y))

# Función para dibujar los elementos del mapa
def map_draw():
    # Crear máscaras para las celdas de pared y suelo
    pared_mask = np.where(mapa == 1, 1, 0)
    suelo_mask = np.where(mapa == 0, 1, 0)
    
    # Calcular el tamaño de una celda en la ventana
    cell_width = WIDTH // columnas
    cell_height = HEIGHT // filas
    
    # Dibujar celdas de pared y suelo
    for fil, col in np.argwhere(pared_mask == 1):
        screen.blit(pared, (col * cell_width, fil * cell_height))
    
    for fil, col in np.argwhere(suelo_mask == 1):
        screen.blit(suelo, (col * cell_width, fil * cell_height))
    
    # Dibujar al robot en función de su dirección
    if direccion == 'derecha' or direccion == 'arriba' or direccion == 'abajo':
        screen.blit(robot, (pos_x * cell_width, pos_y * cell_height))
    elif direccion == 'izquierda':
        screen.blit(robot_left, (pos_x * cell_width, pos_y * cell_height))
    
    # Dibujar la salida en su posición
    screen.blit(out1, (salida_x * cell_width, salida_y * cell_height))
    
    # Mostrar la imagen final cuando el juego ha terminado
    if fin:
        screen.blit(fin_bg, (0, 0))


# Bucle principal
running = True
fin = False
pygame.time.set_timer(MOVE_ROBOT_EVENT, 500)

while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        elif event.type == MOVE_ROBOT_EVENT:
            find_path_bfs()

    map_draw()
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
