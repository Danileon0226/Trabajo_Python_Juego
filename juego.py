import random
import emoji

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

# Función principal del juego
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

# Iniciar el juego
adivina_el_emoji()
