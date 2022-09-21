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
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if button.value == False:
        for x in range(10, 0, -1): # Moves from 10 to 0 in increments of 1
            if x > 0:
                print(f"{x} seconds left!") # Prints the number of seconds left
                r_led.value = True # Turns the red LED on
                time.sleep(.3)
                r_led.value = False # Turns red LED off 0.3 seconds into the 1.0 second cycle.
                time.sleep(.7)
        print(f"Liftoff!") # Since x is not greater than 0, this prints
        g_led.value = True
        time.sleep(2)
        g_led.value = False
