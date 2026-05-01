import pyttsx3
import datetime
# Iniciando Sistemas 
engine = pyttsx3.init()
# Ajustamos la velocidad (150-200 es lo ideal para que se entienda bien)
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def hablar(texto):
    print(f"Asistente: {texto}")
     # Para que también lo veas escrito
    engine.say(texto)
    engine.runAndWait()

    # Prueba
hablar("Hola Luis Manuel, ya tengo voz. Cuál es el siguiente paso?")