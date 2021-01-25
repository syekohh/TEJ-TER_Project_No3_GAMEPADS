from pynput.keyboard import Key, Controller
import time
import serial


portNo = '/dev/tty.usbmodem14101'
keyboard = Controller()

ser = serial.Serial(portNo, 9600)

boolTrue = True

print('boolTrue')

while (boolTrue):
    readVal = str(ser.readline())
    readVal = readVal[2:-5]
    print(readVal)
    # time.sleep(.1)
    if (readVal == 99):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    if (readVal == 97):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    if (readVal == 95):
        keyboard.press('A')
        keyboard.release('A')