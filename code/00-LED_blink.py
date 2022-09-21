# 2022-09-01, Em Heisig (hheisig51)

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while(True):
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5) 