# 2022-10-10, Em Heisig (hheisig51)
# In addition to the previous assignment, 
# this adds an OLED screen to print the values.

import board
import time
import adafruit_mpu6050
import busio
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

sda_pin = board.GP14 # the sda_pin and scl_pin will be used for data
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) # pairs the two pins together

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # creates a variable we can reference for values

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



while True:
    for x in range(1, 5, 1): # Loops a count from 1 to 5
        if x == 4: # 1 out of 5 times, the values are printed
            splash = displayio.Group()
            title = "ANGULAR VELOCITY"
            text_title = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
            content_x = f"x = {round(mpu.acceleration[0],3)},"
            text_x = label.Label(terminalio.FONT, text=content_x, color=0xFFFF00, x=5, y=15)
            content_y = f"y = {round(mpu.acceleration[1],3)},"
            text_y = label.Label(terminalio.FONT, text=content_y, color=0xFFFF00, x=5, y=25)
            content_z = f"z = {round(mpu.acceleration[2],3)}"
            text_z = label.Label(terminalio.FONT, text=content_z, color=0xFFFF00, x=5, y=35)
            splash.append(text_title)
            splash.append(text_x)
            splash.append(text_y)
            splash.append(text_z)
            display.show(splash)
            x = 1
        if mpu.acceleration[2] < 0 and mpu.acceleration[2] > -4: # turns the LED on if x falls within this range
            led.value = True
            time.sleep(.1)
        else:
            led.value = False
            time.sleep(.1)
        