# 2022-09-14, Em Heisig (hheisig51)
# In addition to the previous segments (see 01-countdown.py and 02-lights.py), this assignments adds a button to start the countdown.

import board
import digitalio
import time

g_led = digitalio.DigitalInOut(board.GP18)
r_led = digitalio.DigitalInOut(board.GP13)
g_led.direction = digitalio.Direction.OUTPUT
r_led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16)
button.pull = digitalio.Pull.DOWN

abort = 0

while True:
    if button.value == True:
        if abort == 0:
            break