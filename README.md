# Juego de Laberintos Automático

Este es un juego de laberintos automatizado desarrollado en Python utilizando la biblioteca Pygame. El juego utiliza el algoritmo de búsqueda BFS (Breadth-First Search) para encontrar la ruta más corta desde la posición inicial del robot hasta la salida del laberinto.

## Instalación

1. Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio en tu máquina local utilizando el siguiente comando:
3. Instala las dependencias necesarias ejecutando el siguiente comando:

    ```
    pip install pygame
    ```

## Interacción y Uso

Una vez iniciado el juego, verás al robot moviéndose automáticamente hacia la salida del laberinto utilizando el algoritmo BFS.
No es necesario realizar ninguna interacción manual durante la ejecución del juego. Puedes observar cómo el robot encuentra la salida siguiendo el camino más corto.

## Personalización del Laberinto

Si deseas personalizar el laberinto, puedes hacerlo modificando la matriz `mapa` en el archivo `laberinto.py`. Esta matriz representa el laberinto, donde `0` representa un espacio libre (suelo) y `1` representa una pared.
También puedes cambiar la posición inicial del robot y la posición de la salida modificando las variables `pos_x`, `pos_y`, `salida_x` y `salida_y` en el archivo `laberinto.py`.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, no dudes en compartirlos conmigo.
