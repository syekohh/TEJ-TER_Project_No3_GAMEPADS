from pynput.keyboard import Key, Controller
import time
import serial


def mainnn():

    portNo = '/dev/tty.usbmodem14101'
    keyboard = Controller()

    ser = serial.Serial(portNo, 9600)
    time.sleep(2)

    try:
        readVal = ser.readline()
        print(readVal)
    except serial.SerialException:
        return None

    while readVal == 65:
        time.sleep(2)
        keyboard.pressed('A')
        keyboard.release('A')

