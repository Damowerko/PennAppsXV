#include <Arduino.h>
#include "arduino.h"

// Define various ADC prescaler
const unsigned char PS_16 = (1 << ADPS2);
const unsigned char PS_32 = (1 << ADPS2) | (1 << ADPS0);
const unsigned char PS_64 = (1 << ADPS2) | (1 << ADPS1);
const unsigned char PS_128 = (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);

#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))

double signalAverage = 1024;
int levels[2];

void setup() {
    Serial.begin(115200);
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);

    // setup ADC
    //ADCSRA &= ~PS_16; // remove bits set by arduino lib
    //ADCSRA |= PS_16;     //set prescaler
    sbi(ADCSRA, ADPS2);
    cbi(ADCSRA, ADPS1);
    cbi(ADCSRA, ADPS0);

    // calibrate for ambient noise
    for(int i; i < 5000; i++){
        readSounds(levels);
        updateAverage();
    }
    Serial.println("---READY---\n");
}


#define TOLERANCE 200

void loop() {
    readSounds(levels);

    int minimum = signalAverage+ TOLERANCE;
    char dir = checkLevels(minimum); //returns the speaker which detected the signal
    if(dir){
        long deltaTime = performMeasurement(dir, minimum, 1000, micros());
        if(deltaTime) {

            Serial.println("Measurement Taken!");
            Serial.print(levels[0]);
            Serial.print(", ");
            Serial.print(levels[1]);
            Serial.print("\t");
            Serial.print(dir);
            Serial.print(", ");
            Serial.print(deltaTime); //left-right t
            Serial.print("\t");
            Serial.println(asin(deltaTime*347*0.5/(1000000.0*0.5842)));
        }
        delay(1000);
    } else updateAverage();
    //Serial.println(micros() - time);
}

/// Reads the signals from the ADC.
/// \return pointer to an int array length 2
void readSounds(int *levels){
    levels[0] = analogRead(0);
    levels[1] = analogRead(1);
}

void updateAverage(){
    signalAverage = _updateAverage(levels[0], signalAverage);
    signalAverage = _updateAverage(levels[1], signalAverage);
}

double _updateAverage(int level, double average){
    average = average + 0.001 * (level-average);
    return average;
}

char checkLevels(int minimum){
    if(levels[0] > minimum) return 'L';
    if(levels[1] > minimum) return 'R';
    return 0;
}

long performMeasurement(char originalDir, int minimum, long timeout, long initialTime){
    // pick the appropriate pin for measurement
    int pin = 1;
    if(originalDir == 'R') pin = 0;

    while(levels[pin] < minimum ){
        levels[pin] = analogRead(pin);
        if(micros()-initialTime < timeout){
            return 0;
        }
    }
    return micros()-initialTime;
}
