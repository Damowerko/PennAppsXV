# PennAppsXV: New Ears Eve
New Ears Eve is an aid for the hearing impaired. It alerts users the directions of loud sounds to avoid crises.
## Inspiration
All of our members intimately know people who are hearing impaired. We simply wanted to create something that could make their lives' easier.

## What it does
New Ear's Eve is an aid for deaf people. The goal is to alert the user when there is a loud sound, such as a gun shot or a fire alarm, in order to restore a sense of direction in a crisis. When a sound is heard from a certain location, the belt will vibrate in that direction.

## How we built it
We built this product by first creating a rudimentary microphone to test sample input. We then tweaked the microphone by adding amplifiers, adjusting gain, and writing code. We also laser printed mounting parts that are custom designed to fit snuggly on the belt. We also had to create the electronic components of the belt by connecting wires to the microphone, motor, and Arduinos. We then wrote a substantial amount of code in Python to analyze the sound input from the microphones to estimate the direction of the most likely source of sound. After all the parts were created individually, we attached everything to the belt (a lot of tape was involved).

## Challenges we ran into
Our original plan was to connect the Arduino boards to a Raspberry Pi via USB and have data sent from the Arduino to the Pi. However, the data that the Pi received contained several false positives and often missed signals that the Pi should have gotten. At the last hour of the hackathon we decided to connect the Arduinos to a linux laptop because the laptop had a much more accurate reading of the Arduinos. Another challenge we had was localizing the source of the sound. If we only relied on the loudness of the sound, then we would only be able to make very crude estimates of the source of the sound. However, if we measured the difference in time it takes for each microphone to hear the same sound wave, then we will be able to get a more accurate picture of the sound source. We accomplished this by increasing the sampling rate of the ADC while sacrificing its resolution. We also had an electronics breakdown when the motors mysteriously stopped working. We tried to diagnose the situation by

## Accomplishments that we're proud of
We are proud of belt's sound localization feature. To make this feature as accurate as possible, we first input the distance between two antipodal microphones into the algorithm. Next, the Arduino measures the difference in sound arrival in two opposing microphones. This difference is sent to the computer where it is analyzed. The algorithm will then return an angle that represents the most likely source of sound.

Another great thing about this belt is the electronics. The microphones have fantastic sound recognition quality, the motors vibrate well, and the computer does a great job of localizing the sound of the sound. For having such a short time to develop a product like this, we are proud of its accuracy.

## What's next for New Ears Eve
As of now, our product is a very primitive prototype. What's next is to find better parts and not just use what was around us. Also, the next step would to neaten things up and make it presentable enough to be a distributable product.
