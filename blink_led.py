"""
--------------------------------------------------------------------------
Blink LED USR3
--------------------------------------------------------------------------
License:   
Copyright 2020 Brian Dinh (bad7 [at] rice [dot] edu)

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple code that will 
  - Allow the LED light on the PocketBeagle to blink at a frequency of 5 Hz
    using the Adafruit_BBIO library.

Directions:
  - Connect to the internet using the PocketBeagle
  - Install the Adafruit_BBIO library
  - Run this code on Python 3
  - To stop the code, click CTRL+C and the PocketBeagle will return to its 
    default state

--------------------------------------------------------------------------
"""

import Adafruit_BBIO.GPIO as GPIO
import time

for i in range(4):
    GPIO.setup("USR%d" % 3, GPIO.OUT)

while True:
    for i in range(4):
        GPIO.output("USR%d" % 3, GPIO.HIGH)
        time.sleep(0.2)
    for i in range(4):
        GPIO.output("USR%d" % 3, GPIO.LOW)
        time.sleep(0.2)