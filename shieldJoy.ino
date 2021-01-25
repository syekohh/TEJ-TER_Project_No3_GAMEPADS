// import data file for constants
#include "dataFile.h"

// varibales to reset push button presses
int buttonStateDown = 0;
int buttonStateUp = 0;
int buttonStateLeftClick = 0;

// initialize joystick coordinate variables
int xCor = 0;
int yCor = 0;

// setup code to run once
void setup()
{
    //begin the Serial Monitor at 9600 baud
    Serial.begin(9600);
    //give the Serial a tenth of a second to start up
    delay(100);
    //// set push button pins to INPUT
    pinMode(downArrow, INPUT);
    pinMode(upArrow, INPUT);
    pinMode(mouseLeftClick, INPUT);
}

// loop code to run repeatedly
void loop()
{
    // call the function to read for push buttons
    buttonRead();
    // wait for a tenth of a second
    delay(100);
    // call the function to obtain joystick coordinate points
    readJoy();
}

// function to read the push button states
void buttonRead()
{
    // read all values
    buttonStateDown = digitalRead(downArrow);
    buttonStateUp = digitalRead(upArrow);
    buttonStateLeftClick = digitalRead(mouseLeftClick);

    // if and else-if block to determine which have been pressed
    if (buttonStateUp == HIGH)
    {
        // classify the push button prints different from the joystick coordinate's
        Serial.print("A");
        // print its preset value
        Serial.println(upVal);
        // wait a tenth of a second
        delay(100);
        // reset the value back to LOW or 0 (Zero)
        buttonStateUp = 0;
    }
    else if (buttonStateDown == HIGH)
    {
        // classify the push button prints different from the joystick coordinate's
        Serial.print("A");
        // print its preset value
        Serial.println(downVal);
        // wait a tenth of a second
        delay(100);
        // reset the value back to LOW or 0 (Zero)
        buttonStateDown = 0;
    }
    else if (buttonStateLeftClick == HIGH)
    {
        // classify the push button prints different from the joystick coordinate's
        Serial.print("A");
        // print its preset value
        Serial.println(leftClickVal);
        // wait a tenth of a second
        delay(100);
        // reset the value back to LOW or 0 (Zero)
        buttonStateLeftClick = 0;
    }
}

// function to read joystick coordinates
void readJoy(){

    // read the analog input of each axis
    xCor = analogRead(xInput);
    yCor = analogRead(yInput);

    // only delay for a very short amount of time so there's
    // not alot of wait time between mouse movements
    delayMicroseconds(1);

    // print the x and y coordinates separated by a colon
    Serial.print(xCor);
    Serial.print(":");
    Serial.print(yCor);
    Serial.println();

}