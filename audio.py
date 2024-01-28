#IMPORTAR LA BIBLIOTECA Y CREA UN OBJETO PARA EL RECONOCIMIENTO DE VOZ:
# biblioteca para reconocimiento de voz
import speech_recognition as sr
#objeto Recognizer 
reconocimiento=sr.Recognizer()

#ARCHIVO DE AUDIO
archivo=sr.AudioFile('audioSaludo.wav')

#CAPTURAR LOS DATOS DEL ARCHIVO DE AUDIO
# abrir el archivo de audio 
with archivo as source:
    #grabar y almacenar el archivo de audio en una variable
    audio=reconocimiento.record(source)

#IMPRIMIR EL TEXTO DEL AUDIO
print("Acabas de decir: ")

'''
Realizar el reconocimiento de voz utilizando
el servicio de reconocimiento de voz Google y guardar 
la transcripción del audio en una variable
'''
frase=reconocimiento.recognize_google(audio, language="es-EC")
print(frase)
