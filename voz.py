#IMPORTAR BIBLIOTECAS Y CREA UN OBJETO PARA EL RECONOCIMIENTO DE VOZ:
#biblioteca para el reconocimiento de voz
import speech_recognition as sr
#biblioteca para abrir páginas web
import webbrowser as wb

#objeto Recognizer para realizar tareas de reconocimiento de voz
reconocimiento=sr.Recognizer()

#ESPECIFICAR EL MICRÓFONO COMO ARCHIVOS DE ENTRADA
#Abre el micrófono como fuente de audio y lo asocia con 'source' dentro del bloque
with sr.Microphone() as source:
    #Imprimir un mensaje para indicar que el programa está listo para recibir comandos de voz
    print("Hola en que puedo ayudarte: ")
    #Capturar el audio y almacenarlo en una variable
    audio=reconocimiento.listen(source)

#IMPRIMIR EL TEXTO DEL AUDIO
print("Acabas de decir: ")
'''
Realizar el reconocimiento de voz utilizando
el servicio de reconocimiento de voz Google y guardar 
la transcripción del audio en una variable
'''
frase=reconocimiento.recognize_google(audio,language="es-EC")
print(frase)

#BUSCAR EN GOOGLE
#define la dirección base para realizar búsquedas en Google
url="https://www.google.com/search?q="
#combinar la URL con la frase trasncrita del reconocimiento de voz
buscar=url+frase
#abrir el navegador en la URL construida por la dirección base y comando de voz
wb.open(buscar)

