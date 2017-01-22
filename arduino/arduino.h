//
// Created by damowerko on 1/21/17.
//

#ifndef ARDUINO_ARDUINO_H
#define ARDUINO_ARDUINO_H

void readSounds();
void updateAverage();
double _updateAverage(int level, int average);

char checkLevels(int minimum);
long performMeasurement(char dir, unsigned long timeout);

#endif //ARDUINO_ARDUINO_H