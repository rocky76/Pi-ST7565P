# Pi-ST7565P
ST7565P Graphics LCD Python library for Raspberry Pi, updated for use with Sitronix ST7565P Controller/Driver.
Tested with Crystalfontz CFAG12864U4-NFI LCD Display 

Changes:
1. Default contast changes so image visible.
2. Lowered the voltage so image is visible.
3. Page order corrected for this display.
4. X coordinate shifted from one-based to zero.
5. init() disables all status icons.
6. Reversed dog frames to correct run animation.
7. Updated available contrast range for this family of LCDs.


This was forked from [rdagger](https://github.com/rdagger/Pi-ST7565).  The details below are from his README.md:

# Original README
Tested with Adafruit ST7565 module.
Full tutorial on my website [Rototron](http://www.rototron.info/raspberry-pi-graphics-lcd-display-tutorial/) or click picture below for a YouTube video:

[![ST7565 Tutorial](http://img.youtube.com/vi/Nn5u9xhHCTM/0.jpg)](https://youtu.be/Nn5u9xhHCTM)