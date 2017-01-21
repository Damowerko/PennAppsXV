#include <Arduino.h>

// Define various ADC prescaler
const unsigned char PS_16 = (1 << ADPS2);
const unsigned char PS_32 = (1 << ADPS2) | (1 << ADPS0);
const unsigned char PS_64 = (1 << ADPS2) | (1 << ADPS1);
const unsigned char PS_128 = (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);

void setup() {
    Serial.begin(115200);
    pinMode(A0, INPUT);

    ADCSRA &= ~PS_16; // remove bits set by arduino lib

    ADCSRA |= PS_16; //set prescaler
}



void loop() {

}