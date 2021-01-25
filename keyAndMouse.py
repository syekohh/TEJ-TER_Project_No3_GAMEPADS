# import all necessary libraries
from pynput.mouse import Button
from pynput.mouse import Controller as mouseControl
from pynput.keyboard import Key
from pynput.keyboard import Controller as keyboardControl
import time
import serial

# save the port number as a String
portNo = '/dev/tty.usbmodem14101'

# set the ser varibale to connect to the Serial Monitor
ser = serial.Serial(portNo, 9600)

# initialize controllers for keyboard and mouse
keyboard = keyboardControl()
mouse = mouseControl()

# xMax = 1280
# yMax = 800

# initialize the initial values for X and Y coordinates on screen
X = 640
Y = 400
# set the cursor/mouse to be on the center of the screen
mouse.position = (X, Y)

# define constant True varibale to keep the loop running
boolTrue = True

# loop to keep running and reading values from the Serial Monitor
while (boolTrue):
    # save the read value from the Serial Monitor as a String
    readVal = str(ser.readline())
    # substring out the unecessary characters picked up
    readVal = readVal[2:-5]
    # print this value to the terminal
    print(readVal)
    # if the push button classifier is met, run this 'if' block
    if (readVal[0] == 'A'):
        # if the up arrow specifier is recognized, press the up arrow
        if (readVal[-2:] == '99'):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        # if the down arrow specifier is recognized, press the down arrow
        if (readVal[-2:] == '97'):
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        # if the left click specifier is recognized, left click
        if (readVal[-2:] == '95'):
            mouse.click(Button.left, 1)
    # otherwise, read the joystick info
    else :
        # get the 'x' and 'y' values from the joystick/Serial Monitor
        (x, y) = readVal.split(':')
        # turn them into integers (from Strings)
        x = int(x)
        y = int(y)

        # if statements to classify direction of movement (or no movement)
        # still (no movement)
        if (((x > 495) and (x < 505)) and ((y > 495) and (y < 505))):
            mouse.position = (X, Y)
        # top right
        if ((x > 750) and (y > 750)):
            X+=7
            Y-=7
            mouse.position = (X, Y)
        # bottom right
        if ((x > 750) and (y < 750)):
            X+=7
            Y+=7
            mouse.position = (X, Y)
        # bottom left
        if ((x < 250) and (y < 250)):
            X-=7
            Y+=7
            mouse.position = (X, Y)
        # top left
        if ((x < 750) and (y > 750)):
            X-=7
            Y-=7
            mouse.position = (X, Y)