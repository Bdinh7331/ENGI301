Author: Brian Dinh

The goal of this project was to create a PCB of my first project, IcyHot, were I have successfully completed it. Upon consulting with my professor, Erik Welsh, he suggested
that I add in the LED screen that I was unable to integrate during my first project. This project is associated with Rice University's Introduction to Practical Electrical
Engineering course, also known as ENGI 301.

This project uses the following libraries:
1. ENGI301, created by Erik Welsh
2. nf-a4x20-5v-pwm, a custom library created by myself to house the Noctua fan
3. adafruit, which came with EAGLE

To complete this project, I did the following steps:
1. Created a schematic using existing Pocketbeagle, LED screen, and temperature sensors from the ENGI301 and adafruit libraries
2. Made a board on EAGLE using that schematic. This board was initially 3x4 as suggested by Professor Welsh, but I increased the dimensions to 3.5x4 to fit all of my components.
  -Because of how my components were organized in the board, I routed my components in the top and bottom layers instead of just the top layer.
  -I added as few drill holes as possible, though they were unavoidable because of how the routing was laid out on this board.
3. Prepared a gerber file for manufacturing
  -Exported my IcyHot.brd file as a CAM output, labelling it as "IcyHot_gerber."
  -Downloaded gerbv, an open source gerber reader, to provide a screenshot of the top and bottom layers of the PCB which is located in the "docs" folder of this directory.
  -Created an account at openfab.
4.
