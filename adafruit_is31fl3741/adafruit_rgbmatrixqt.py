# SPDX-FileCopyrightText: Tony DiCola 2017 for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_is31fl3741.adafruit_rgbmatrixqt`
====================================================

CircuitPython driver for the Adafruit IS31FL3741 RGB Matrix QT board


* Author(s): ladyada

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

# imports
from . import IS31FL3741

REMAP = bytes([8, 5, 4, 3, 2, 1, 0, 7, 6])


class Adafruit_RGBMatrixQT(IS31FL3741):
    """Supports the ISSI IS31FL3741 eval board"""

    width = 13
    height = 9

    @staticmethod
    def pixel_addrs(x, y):
        """Calculate the RGB offsets into the device array for x,y pixel"""
        col = x
        row = REMAP[y]

        if row <= 5:
            if col < 10:
                offset = 0x1E * row + col * 3
            else:
                offset = 0xB4 + 0x5A + 9 * row + (col - 10) * 3
        else:
            if col < 10:
                offset = 0xB4 + (row - 6) * 0x1E + col * 3
            else:
                offset = 0xB4 + 0x5A + 9 * row + (col - 10) * 3

        if col == 12 or col % 2 == 1:  # odds + last col
            # r=2, g=1, b=0
            return offset + 2, offset + 1, offset
        return offset, offset + 2, offset + 1
