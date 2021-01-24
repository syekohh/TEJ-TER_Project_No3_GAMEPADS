from pynput.mouse import Button, Controller as mouseControl
from pynput.keyboard import Key, Controller as keyboardControl
import time
import serial

portNo = '/dev/tty.usbmodem14101'

ser = serial.Serial(portNo, 9600)

boolTrue = True

while (boolTrue):
    readVal = str(ser.readline())
    if (readVal[0] == 'A'):
        if (readVal[-2:] == '99'):
            keyboardControl.press(Key.up)
            keyboardControl.release(Key.up)
        if (readVal[-2:] == '97'):
            keyboardControl.press(Key.down)
            keyboardControl.release(Key.down)
        if (readVal[-2:] == '95'):
            keyboardControl.press('A')
            keyboardControl.release('A')
    else :
        pass

