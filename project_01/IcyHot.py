""""
#!/bin/bash
# --------------------------------------------------------------------------
# IcyHot- Fan and Thermometer System
# --------------------------------------------------------------------------
# License:   
# Copyright 2020 Brian Dinh
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------

Use the PocketBeagle to program a fan-temperature sensor apparatus consisting
of 2 fans, 1 thermal sensor, and 1 screen to display the local temperature.

**Screen not coded properly as of 11-13-20 at 11:59 PM CT. I'm currently working
on that as quickly as possible**

Requirements:
  -  Internet connection
  -  PocketBeagle
  -  iii

Uses:
  - 2 NF-A4x20 5V PWM 40x20mm PREMIUM FAN
  - Adafruit Si7021 Tempreature & Humidity Sensor
  - 2.8" TFT LCD w/Touchscreen
  - Libraries below:
    - Adafruit CircuitPython SI7021
    - Adafruit PIL
  
Attribution:
  - Github user enwi for their code fan_control.py, which controls fan speed
  - Professor Erik Welsh for walking me through how to navigate these libraries
  - Two fellow mechanical engineering students at Rice- Odnan Galvin and
    Nicholas Lester- who had previously taken ENGI 301, for explaining extra 
    software concepts
"""
"""
Temperature Sensors
"""
import time
import board
import busio
from busio import I2C
from board import SCL, SDA
import adafruit_si7021


# Create library object using our Bus I2C port
config-pin P1_28 i2c
config-pin P1_26 i2c
i2c = busio.I2C("P1_28", "P1_26")
sensor = adafruit_si7021.SI7021(i2c)


while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
  time.sleep(2)



"""
Fans
"""
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import os
import signal
import time


# For fan 1:
c_FAN_1 = "P2_1"					# pwm pin fan 1 is connected to
c_FAN_TACHO_1	= "P2_4"			# gpio pin fan 1's tachometer is connected to
c_MIN_TEMPERATURE_1 = 0		# temperature in degrees c when fan 1 should turn on
c_TEMPERATURE_OFFSET_1 = 2	# temperarute offset in degrees c when fan 1 should turn off

# For fan 2:
c_FAN_2 = "P1_36"					# pwm pin fan 2 is connected to
c_FAN_TACHO_2	= "P1_33"			# gpio pin fan 2's tachometer is connected to
c_MIN_TEMPERATURE_2 = 0		# temperature in degrees c when fan should turn on
c_TEMPERATURE_OFFSET_2 = 2	# temperarute offset in degrees c when fan should turn off

# Advanced configuration
c_PWM_FREQUENCY = 20		# frequency of the pwm signal to control the fan with
c_PWM_POL = 0    # polarity of the pwm signal 0

GPIO.setup("P2_4", GPIO.IN)
GPIO.setup("P1_33", GPIO.IN)
PWM.start("P2_1", 80, c_PWM_FREQUENCY, c_PWM_POL) # starts fan 1
PWM.start("P1_36", 80, c_PWM_FREQUENCY, c_PWM_POL) # starts fan 2

# Clean up GPIOs
GPIO.cleanup()

# Stop fans
PWM.stop("P2_1")
PWM.stop("P1_36")
PWM.cleanup()

"""
LCD SCREEN
"""
import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341

# Initial setup
BORDER = 20
FONTSIZE = 24
spi = board.SPI()
cs_pin = 'P1_06'
dc_pin = "P1_04"
BAUDRATE = 24000000
disp = ili9341.ILI9341(
    spi,
    rotation=90,  # 2.2", 2.4", 2.8", 3.2" ILI9341
    cs=cs_pin,
    dc=dc_pin,
    baudrate=BAUDRATE)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Load a TTF Font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
 
# Draw Some Text
text = "Hello World!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (width // 2 - font_width // 2, height // 2 - font_height // 2),
    text,
    font=font,
    fill=(255, 255, 0),
)
 
# Display image.
disp.image(image)
