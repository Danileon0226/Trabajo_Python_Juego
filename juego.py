import random
import emoji
import sys
import pygame

# Lista de emojis para adivinar
emojis = {
    "sonrisa": "😀",
    "coche": "🚗",
    "pizza": "🍕",
    "sol": "🌞",
    "pastel": "🎂",
    "fiesta": "🎉",
    "cámara": "📷",
    "arcoíris": "🌈",
    "gato": "🐱",
    "helado": "🍦"
}

# Función para seleccionar un emoji aleatorio
def seleccionar_emoji():
    palabra_clave, emoji_seleccionado = random.choice(list(emojis.items()))
    return palabra_clave, emoji_seleccionado

# Función principal del juego de adivinar el emoji
def adivina_el_emoji():
    print("Bienvenido al juego Adivina el Emoji")
    print("Tienes que adivinar el emoji a partir de su descripción")
    
    intentos = 3
    
    while intentos > 0:
        palabra_clave, emoji_seleccionado = seleccionar_emoji()
        print(f"Intentos restantes: {intentos}")
        print("Descripción:", palabra_clave.capitalize())
        
        adivinanza = input("Escribe tu adivinanza (palabra clave o 'salir' para salir): ").lower()
        
        if adivinanza == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        
        if adivinanza == palabra_clave:
            print(f"¡Felicidades! Has adivinado el emoji correctamente: {emoji.emojize(emoji_seleccionado)}")
            intentos = 3  # Reiniciar los intentos
        else:
            intentos -= 1
            if intentos > 0:
                print("Respuesta incorrecta. Inténtalo de nuevo.")
            else:
                print(f"Lo siento, has agotado tus intentos. El emoji era: {emoji.emojize(emoji_seleccionado)}")

# Función principal del juego de la serpiente
def juego_de_serpiente():
    pygame.init()
    ancho, alto = 640, 480
    pantalla = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()

    NEGRO = (0, 0, 0)
    VERDE = (0, 255, 0)

    tamano_celda = 20
    serpiente = [(ancho // 2, alto // 2)]
    direccion = (1, 0)
    comida = (random.randint(0, ancho // tamano_celda - 1) * tamano_celda,
              random.randint(0, alto // tamano_celda - 1) * tamano_celda)

    def dibujar_serpiente(serpiente):
        for segmento in serpiente:
            pygame.draw.rect(pantalla, VERDE, (segmento[0], segmento[1], tamano_celda, tamano_celda))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != (0, 1):
                    direccion = (0, -1)
                elif evento.key == pygame.K_DOWN and direccion != (0, -1):
                    direccion = (0, 1)
                elif evento.key == pygame.K_LEFT and direccion != (1, 0):
                    direccion = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direccion != (-1, 0):
                    direccion = (1, 0)

        nueva_cabeza = (serpiente[0][0] + direccion[0] * tamano_celda, serpiente[0][1] + direccion[1] * tamano_celda)
        serpiente.insert(0, nueva_cabeza)

        if serpiente[0] == comida:
            comida = (random.randint(0, ancho // tamano_celda - 1) * tamano_celda,
                      random.randint(0, alto // tamano_celda - 1) * tamano_celda)
        else:
            serpiente.pop()

        if (serpiente[0][0] < 0 or serpiente[0][0] >= ancho or
            serpiente[0][1] < 0 or serpiente[0][1] >= alto or
            serpiente[0] in serpiente[1:]):
            pygame.quit()
            sys.exit()

        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, VERDE, (*comida, tamano_celda, tamano_celda))
        dibujar_serpiente(serpiente)
        pygame.display.flip()
        reloj.tick(10)

# Función del menú principal
def menu_principal():
    while True:
        print("Menu")
        print("1. Adivina el emoji")
        print("2. Juego de la serpiente")
        print("3. Salir")
    
        seleccion = input("Seleccionar una opcion:")
    
        if seleccion == "1":
            print("Has seleccionado la Opción 1.")
            adivina_el_emoji()
        elif seleccion == "2":
            print("Has seleccionado la Opción 2.")
            juego_de_serpiente()
        elif seleccion == "3":
            print("Saliendo del programa.")
            break  # Salir del bucle while
        else:
            print("Selección no válida. Por favor, selecciona una opción válida.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
