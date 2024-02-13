import serial
import pyautogui
import os

# Puerto COM y velocidad en baudios
puerto = "COM6"
baudios = 9600

# Señal a detectar
senal_esperada = "a"

# Abrir el puerto COM
s = serial.Serial(puerto, baudios)


while True:
    print("Listening in...", puerto)
    # Leer datos del puerto
    linea = s.readline().decode("utf-8")

    # Si se recibe la señal esperada, ejecutar la acción
    if linea.strip() == senal_esperada:
        print("¡ADVERTENCIA MOVIMIENTO DETECTADO!")
        # **Aquí se coloca la acción a ejecutar**
        pyautogui.hotkey("alt","tab")


# Cerrar el puerto COM
s.close()