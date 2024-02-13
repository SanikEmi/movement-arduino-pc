#include <SoftwareSerial.h>
SoftwareSerial Bluetooth(10, 11); //RX and TX HC05 sensor
int valor;

void setup() {
  // put your setup code here, to run once:
Bluetooth.begin(9600);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(1);
 
  if(valor < 750){
    Bluetooth.println("a");
    //Serial.println(valor);
    delay(2800);
      }
      
}



