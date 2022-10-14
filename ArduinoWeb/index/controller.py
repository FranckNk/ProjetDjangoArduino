from pyfirmata2 import Arduino, util, INPUT
import time

PORT = Arduino.AUTODETECT
board = Arduino(PORT)


def blueOn():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(0)

def redOn():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[6].write(0)

def greenOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[6].write(0)


def yellowOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(1)

def allOff():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[6].write(0)
def AllOn():
    board.digital[2].write(1)
    board.digital[3].write(1)
    board.digital[4].write(1)
    board.digital[6].write(1)

def readValue(pin):
    board.analog[pin].mode = INPUT
    it = util.Iterator(board)
    it.start()
    board.analog[pin].enable_reporting()
    valeur = board.analog[pin].read()
    print("La valeur lue est : ")
    print(valeur)

def blinkall():
    count = 10
    while (count > 0):
        AllOn()
        time.sleep(0.6)
        allOff()
        time.sleep(0.6)
        count = count - 1