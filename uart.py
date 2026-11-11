import serial
import time

# Windows : "COM3" ; Linux : "/dev/ttyACM0" ; macOS : "/dev/cu.usbmodem..."
ser = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)  # l'Arduino redémarre à l'ouverture du port

try:
    while True:
        ligne = ser.readline().decode().strip()
        if ligne:
            valeur = int(ligne)
            print(f"Mesure : {valeur}")
            # Seuil : LED allumée si la valeur dépasse 512
            ser.write(b"1" if valeur > 512 else b"0")
except KeyboardInterrupt:
    ser.close()