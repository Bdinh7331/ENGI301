Build directions:
1. Collect the required materials: 
      2x Noctua NF-A4x20 5V PWM, Premium Quiet Fan, 4-Pin, 5V Version (40x20mm, Brown)
      1x 2.8" Color TFT LCD display with MicroSD Card Breakout - ST7735R
      25-30x Jumper wires
      2x Adafruit Si2071 Temperature & Humidity Pressure Sensor 
      1x Regular generic breadboard
      2x Small generic breadboards
      1x PocketBeagle as the microcontroller
      1x USB cable to connect the PocketBeagle to a computer
2. Solder five pins to each of the five holes in both temperature/humidity sensors, you are given six pins so you will need to remove one before soldering
3. Follow the pin convention as described below:
   Fan 1 Connections:
    PWM --> P1_36
    TACH --> P1_33
    GND --> P1_22
    VOUT --> P1_24
  Fan 2 Connections:
    PWM --> P2_1
    TACH --> P2_4
    GND --> P2_15
    VOUT --> P2_13
  Temperature & Humidity Sensor 1 Connections:
    GND --> GND
    VIN --> 3.3V
    SCL --> P1_28
    SDA --> P1_26
    Note: 1k Ohm pull up to 3.3V for SCL and 1k Ohm pull up to 3.3V for SDA
  Temperature & Humidity Sensor 1 Connections:
    GND --> GND
    VIN --> 3.3V
    SCL --> P2_9
    SDA --> P2_11
    Note: 1k Ohm pull up to 3.3V for SCL and 1k Ohm pull up to 3.3V for SDA
  LCD Display Connections:
    CLK --> P1_8
    MISO --> P1_10
    MOSI --> P1_12
    CS --> P1_6
    D/C --> P1_4
    Note: Circuit is completed by GND --> P1_16 and VOUT --> P1_14
    
Operating Instructions:
4. Co
