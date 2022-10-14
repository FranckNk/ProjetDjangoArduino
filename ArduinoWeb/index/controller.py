import pyfirmata2
import time

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)


def blueOn():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)

def redOn():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)

def greenOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)


def yellowOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)

def allOff():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
def AllOn():
    board.digital[2].write(1)
    board.digital[3].write(1)
    board.digital[4].write(1)
    board.digital[5].write(1)

def blinkall():
    count = 10
    while (count > 0):
        AllOn()
        time.sleep(0.5)
        allOff()
        time.sleep(0.5)
        count = count - 1