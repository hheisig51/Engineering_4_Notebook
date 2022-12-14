# 2022-09-29, Em Heisig (hheisig51)
# This assignment just prints x, y, and z acceleration
# values from an MPU-6050 chip to the serial monitor.

import board
import time
import adafruit_mpu6050
import busio

sda_pin = board.GP14 # the sda_pin and scl_pin will be used for data
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) # pairs the two pins together

mpu = adafruit_mpu6050.MPU6050(i2c) # creates a variable we can reference for values

while True: # cleans up and prints the x, y, and z values
    print(f"x = {round(mpu.acceleration[0],3)}, y = {round(mpu.acceleration[1],3)}, z = {round(mpu.acceleration[2],3)}")
    time.sleep(.5)