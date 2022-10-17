#include <Arduino.h>
#include <Adafruit_AHTX0.h>

Adafruit_AHTX0 aht;

void setup() {
  Serial.begin(9600);

  if (! aht.begin()) {
  }
}

void loop() {
  sensors_event_t humidity, temp;
  aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data

  Serial.print(temp.temperature);
  Serial.print("x"); 
  Serial.println(humidity.relative_humidity); 

  delay(1000);
}