from pynput.keyboard import Key, Controller
import time
import serial


portNo = '/dev/tty.usbmodem14101'
keyboard = Controller()

ser = serial.Serial(portNo, 9600)

boolTrue = True

while (boolTrue):
    readVal = int(ser.readline())
    # time.sleep(.1)
    if (readVal == 66):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    if (readVal == 65):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    if (readVal == 3):
        keyboard.press('A')
        keyboard.release('A')