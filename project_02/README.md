Author: Brian Dinh

The goal of this project was to create a PCB of my first project, IcyHot, were I have successfully completed it. Upon consulting with my professor, Erik Welsh, he suggested
that I add in the LED screen that I was unable to integrate during my first project. This project is associated with Rice University's Introduction to Practical Electrical
Engineering course, also known as ENGI 301.

This project uses the following libraries:
1. ENGI301, created by Erik Welsh
2. IcyHot, a custom library created by myself to house the Noctua fan and switch
3. adafruit, which came with EAGLE

To complete this project, I did the following steps:
1. Created a schematic using existing Pocketbeagle, LED screen, and temperature sensors from the three aforementioned libraries.
  -To create the nf-a4x20-5v-pwm (Noctua fan) component, I made a box with 4 pins that was about the physical dimensions of the base of the fan. Since the datasheet did not provide any additional information about how the pins were oriented, I spaced them out by about 100 mil.
  -To create the switch, I followed the exact guidelines provided by its datasheet.
2. Made a board on EAGLE using that schematic. This board was initially 3x4 as suggested by Professor Welsh, but I increased the dimensions to 3.5x4 to fit all of my components.
  -Because of how my components were organized in the board, I routed my components in the top and bottom layers instead of just the top layer.
  -I added as few drill holes as possible, though they were unavoidable because of how the routing was laid out on this board.
3. Prepared a gerber file for manufacturing
  -Exported my IcyHot.brd file as a CAM output, labelling it as "IcyHot_gerber."
  -Downloaded gerbv, an open source gerber reader, to provide a screenshot of the top and bottom layers of the PCB which is located in the "docs" folder of this directory.
  -Created an account at MacroFab.
4. Got quotes for 1, 10, 100, and 1000 PCBs with my components on MacroFab.
  -Substituted another 5V PWM fan for the Noctua because Noctua fans are not available on MacroFab. This affects the price though the fan was not the most expensive component.
  -Prices were much larger than expected since many of the components had very large lead times and/or were not immediately available.

Design Philosophy
  The design philosophy that I used during this project was essentially to keep everything as simple as possible since this is good engineering practice. Because the goal of this project was to put the components that I had used in the first ENGI 301 project onto a PCB, I wanted to replicate the exact components as much as possible. Some specific ways of how I ensured that the schematic would be simple was that I would only create library parts from scratch only when it was absolutely necessary. As several components had schematics, libraries, and boards already available on open source platforms
