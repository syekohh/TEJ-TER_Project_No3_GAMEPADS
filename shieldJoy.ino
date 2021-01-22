int BUTTONstate1 = 0;
int BUTTONstate2 = 0;
int BUTTONstate3 = 0;

int first = 65;
int second = 66;
int third = 3;
void setup()
{
    Serial.begin(9600);
    pinMode(10, INPUT);
    pinMode(11, INPUT);
    pinMode(12, INPUT);
}
void loop()
{
    //Serial.println("");
    BUTTONstate1 = digitalRead(10);
    BUTTONstate2 = digitalRead(11);
    BUTTONstate3 = digitalRead(12);
    if (BUTTONstate1 == HIGH)
    {
        Serial.println(first);
        delay(1000);
        BUTTONstate1 = 0;
    }
    else if (BUTTONstate2 == HIGH)
    {
        Serial.println(second);
        delay(1000);
        BUTTONstate2 = 0;
    }
    else if (BUTTONstate3 == HIGH)
    {
        Serial.println(third);
        delay(1000);
        BUTTONstate2 = 0;
    }
}