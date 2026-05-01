mport speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time

# Configuración del reconocimiento de voz
r = sr.Recognizer()

# configuración voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# 🎤 GRABAR AUDIO (sin PyAudio)
def grabar_audio():
    fs = 44100
    print("🎤 Escuchando...")
    audio = sd.rec(int(3 * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    audio = (audio * 32767).astype(np.int16)
    write("audio.wav", fs, audio)

# 🔥 ACTIVAR JARVIS
def escuchar_palabra_activacion():
    grabar_audio()
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)

    try:
        texto = r.recognize_google(audio, language='es')
        print("Detectado:", texto)
        if 'jarvis' in texto.lower():
            return True
    except:
        return False
    return False

# 🔥 ESCUCHAR COMANDO
def escuchar_comando():
    grabar_audio()
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)

    try:
        texto = r.recognize_google(audio, language='es')
        print("Comando detectado:", texto)
        return texto.lower()
    except:
        return ""

# 🗣️ HABLAR
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

activado = False

while True:
    if not activado:
        print("Di jarvis para activarme...")
        if escuchar_palabra_activacion():
            activado = True
            hablar("Sí, ¿en qué puedo ayudarte?")
    else:
        comando = escuchar_comando()
        
        if comando == "":
            hablar("No detecto ningún comando")

        elif 'apagar' in comando:
            hablar("Hasta pronto, apagado")
            break

        # 🔥 MEJORA PARA CANCIONES ESPECÍFICAS
        elif 'reproduce' in comando:
            cancion = comando.replace('reproduce', '')
            cancion = cancion.replace('canción de', '')
            cancion = cancion.replace('musica de', '')
            cancion = cancion.replace('una canción de', '')
            cancion = cancion.strip()

            hablar("Reproduciendo " + cancion)
            pywhatkit.playonyt(cancion + " oficial")

        elif 'hora' in comando:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            hablar("La hora actual es: " + hora_actual)

        else:
            hablar("No entendí ese comando")
        
        time.sleep(1)