from pynput.mouse import Button, Controller
import time
import serial


# portNo = '/dev/tty.usbmodem14101'
mouse = Controller()
xMax = 1280
yMax = 800
x = 0
y = 0
# ser = serial.Serial(portNo, 9600)

boolTrue = True

while (boolTrue):
    # readVal = int(ser.readline())
    mouse.position = (x, y)
    time.sleep(.005)
    if (x < xMax):
        x+=1
    else :
        boolTrue = False
    if (y < yMax):
        y+=1
    else :
        boolTrue = False
