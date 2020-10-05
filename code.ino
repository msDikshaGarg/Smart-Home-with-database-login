#include <Servo.h>
#include <EEPROM.h>

Servo servo;
char state;

void setup() {
  
  servo.attach(7);

  if(EEPROM.read(0) == 1)
  {                      
    servo.write(70); 
    delay(200);
  }
  else if(EEPROM.read(0) == 2)
  {
    servo.write(120); 
    delay(200);
  }
  
  Serial.begin(9600);
}

void loop() {
 
  if(Serial.available() > 0)
  {
    char data;
    data = Serial.read();
    Serial.print(data);
    switch(data)
    {
      case '1': 
        if(EEPROM.read(0) == 1) 
        {
          EEPROM.write(0, 2);
          Serial.print("3");
          for(int a = 70; a <= 120; a++) 
          {
            servo.write(a);
            delay(15);
            Serial.println(servo.read());
          }
        }
        else if(EEPROM.read(0) == 2)
        {
          EEPROM.write(0, 1); 
          Serial.print("4"); 
          for(int x = 120; x >= 70; x--)
          {
            servo.write(x);
            delay(15);
          }
        }
        break;
      case '3': 
     
        if(EEPROM.read(0) == 1)
        {
          Serial.print("4");
        }
        else if(EEPROM.read(0) == 2)
        {
          Serial.print("3");
        }
        break;
    }
  }
  
}
