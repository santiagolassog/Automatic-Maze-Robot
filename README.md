# Juego de Laberintos Automático con Pygame

¡Embárcate en una emocionante aventura en el mundo de los videojuegos con Python y Pygame! Sumérgete en un desafío de destreza y lógica mientras guías a un robot a través de un laberinto en una ventana de **500x500 píxeles**. Personaliza tu experiencia con tus propias imágenes de paredes y suelos, y observa cómo el robot encuentra el camino más corto hacia la salida. ¿Tienes lo necesario para conquistar este laberinto automatizado?

## Demostración

<table>
  <tr>
    <td><img src="https://github.com/santiagolassog/Juego-de-Laberintos-Automatico-con-Pygame/assets/27078128/584dcd91-5326-451b-8611-dc078e986dac" alt="Laberinto 1"></td>
    <td><img src="https://github.com/santiagolassog/Juego-de-Laberintos-Automatico-con-Pygame/assets/27078128/5e816e6a-2230-4914-b45c-67185c68e0c0" alt="Laberinto 2"></td>
  </tr>
</table>

<table>
  <tr>
    <td><img src="https://github.com/santiagolassog/Juego-de-Laberintos-Automatico-con-Pygame/assets/27078128/f305a264-00fd-492d-886f-f6046c273eff" alt="Laberinto 3"></td>
    <td><img src="https://github.com/santiagolassog/Juego-de-Laberintos-Automatico-con-Pygame/assets/27078128/0b69a650-6ba2-4944-9b6e-74f1e0a804c5" alt="Laberinto 4"></td>
  </tr>
</table>

## Instalación

1. Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio en tu máquina local utilizando el siguiente comando:
3. Instala las dependencias necesarias ejecutando el siguiente comando:

    ```
    pip install pygame
    ```

## Estructura del Proyecto

- **`Images/`**: Contiene las imágenes utilizadas en el juego.
- **`laberinto.py`**: El script principal que contiene el código del juego.
  
## Funcionalidades

- **Exploración Automatizada:** El robot encuentra automáticamente el camino más corto hacia la salida utilizando el algoritmo BFS (Breadth-First Search).
- **Personalización del Laberinto:** Modifica la configuración del laberinto cambiando la matriz de mapa y la posición inicial del robot.
- **Interfaz Gráfica Atractiva:** Disfruta de gráficos atractivos gracias a la biblioteca Pygame.

## Interacción y Uso

Una vez iniciado el juego, verás al robot moviéndose automáticamente hacia la salida del laberinto utilizando el algoritmo BFS.
No es necesario realizar ninguna interacción manual durante la ejecución del juego. Puedes observar cómo el robot encuentra la salida siguiendo el camino más corto.

## Personalización del Laberinto

Si deseas personalizar el laberinto, puedes hacerlo modificando la matriz `mapa` en el archivo `laberinto.py`. Esta matriz representa el laberinto, donde `0` representa un espacio libre (suelo) y `1` representa una pared.
También puedes cambiar la posición inicial del robot y la posición de la salida modificando las variables `pos_x`, `pos_y`, `salida_x` y `salida_y` en el archivo `laberinto.py`.

## Agradecimientos

Agradezco a la comunidad de Pygame y a los recursos en línea que ayudaron a desarrollar este juego. ¡La aventura y la diversión te esperan en este emocionante laberinto automatizado!

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, no dudes en compartirlos conmigo.
