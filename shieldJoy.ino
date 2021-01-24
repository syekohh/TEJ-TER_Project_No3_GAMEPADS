#include "dataFile.h"

int BUTTONstateDown = 0;
int BUTTONstateUp = 0;
int BUTTONstateClick = 0;

int xCor = 0;
int yCor = 0;

void setup()
{
    Serial.begin(9600);
    delay(100);
    pinMode(downArrow, INPUT);
    pinMode(upArrow, INPUT);
    pinMode(mouseClick, INPUT);
}
void loop()
{
    arrowRead();
    delay(100);
    readJoy();
}

void arrowRead()
{
    BUTTONstateDown = digitalRead(downArrow);
    BUTTONstateUp = digitalRead(upArrow);
    BUTTONstateClick = digitalRead(mouseClick);

    if (BUTTONstateUp == HIGH)
    {
        Serial.print("A");
        Serial.println(upVal);
        delay(100);
        BUTTONstateUp = 0;
    }
    else if (BUTTONstateDown == HIGH)
    {
        Serial.print("A");
        Serial.println(downVal);
        delay(100);
        BUTTONstateDown = 0;
    }
    else if (BUTTONstateClick == HIGH)
    {
        Serial.print("A");
        Serial.println(clickVal);
        delay(100);
        BUTTONstateClick = 0;
    }
}

void readJoy(){

    xCor = analogRead(xInput);
    yCor = analogRead(yInput);

    delay(1000);

    Serial.print(xCor);
    Serial.print(":");
    Serial.print(yCor);
    Serial.println();

}