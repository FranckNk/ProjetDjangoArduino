from pyfirmata2 import Arduino, util, INPUT
from index.models import *
import serial
import schedule
import time



def blueOn():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(0)
    board.exit()

def redOn():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[6].write(0)
    board.exit()

def greenOn():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[6].write(0)
    board.exit()


def yellowOn():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(1)
    board.exit()

def allOff():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(0)
    board.exit()
    
def AllOn():
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.digital[2].write(1)
    board.digital[3].write(1)
    board.digital[4].write(1)
    board.digital[6].write(1)
    board.exit()

def readValue(pin):
    """
    PORT = Arduino.AUTODETECT
    board = Arduino(PORT)

    board.analog[pin].mode = INPUT
    it = util.Iterator(board)
    it.start()
    board.analog[pin].enable_reporting()
    valeur = board.analog[pin].read()
    print("La valeur lue est : ")
    print(valeur)
    Capteur = AHT20()
    Capteur.temperature = valeur * 10
    Capteur.humidite = valeur * 100
    Capteur.save()
    board.exit()
    """
    
    ser = serial.Serial("COM3")
    print(ser.name)
    text = ""
    text = ser.read(20)
    print("La chaine lue -> : " )
    print(text)
    ser.close()

def blinkall():
    count = 10
    while (count > 0):
        AllOn()
        time.sleep(0.6)
        allOff()
        time.sleep(0.6)
        count = count - 1
        
def fonction():
    list_values = []
    list_in_floats = []
    arduino = serial.Serial('COM3', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))

    print(f'Collected readings from Arduino: {list_in_floats}')

    Val = AHT20.objects.all()
    Val.delete()
    Capteur = AHT20()
    Capteur.temperature = list_in_floats[0]
    Capteur.humidite = list_in_floats[1]
    Capteur.save()
    
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')