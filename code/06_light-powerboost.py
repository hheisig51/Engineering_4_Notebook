# 2022-10-03, Em Heisig (hheisig51)
# In this assignment, a red LED lights up if {x} is within 
# a certain range (Acceleration of 0 to -4, which rougly 
# corresponds with a rotation of 90 degrees)

import board
import time
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14 # the sda_pin and scl_pin will be used for data
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) # pairs the two pins together

mpu = adafruit_mpu6050.MPU6050(i2c) # creates a variable we can reference for values

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

x = 1

while True:
    for x in range(1, 5, 1): # Loops a count from 1 to 5
        if x == 4: # 1 out of 5 times, the values are printed
            print(f"x = {round(mpu.acceleration[0],3)}, y = {round(mpu.acceleration[1],3)}, z = {round(mpu.acceleration[2],3)}")
            x = 1
        if mpu.acceleration[2] < 0 and mpu.acceleration[2] > -4: # turns the LED on if x falls within this range
            led.value = True
            time.sleep(.1)
        else:
            led.value = False
            time.sleep(.1)
