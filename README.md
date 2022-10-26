# Engineering_4_Notebook

- [About](#about)

## Circuit Python Table of Contents

- [Pico](#pico)

### Launch Pad

- [Countdown](#countdown-launch-pad-1)
- [Lights](#lights-launch-pad-2)
- [Button](#button-launch-pad-3)
- [Servo](#servo-launch-pad-4)

### Crash Avoidance

- [Accelerometer](#accelerometer-crash-avoidance-1)
- [Light & Powerboost](#light-and-powerboost-crash-avoidance-2)
- [OLED](#oled-crash-avoidance-3)

### Landing Area

- [Functions](#functions-landing-area-1)
- [Plotting](#plotting-landing-area-2)

## CAD Table of Contents

- [Ring & Spinner](#ring-and-spinner-cad-1)
- [Key & Prop](#key-and-prop-cad-2)
- [Assembling the Launcher](#assembling-the-launcher-cad-3)

## Pico

These assignments were completed on a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) microcontroller, running [Circuit Python](https://circuitpython.org/board/raspberry_pi_pico/) 7.3.2

## Countdown (Launch Pad #1)

### Countdown Description

The purpose of this assignment is to print a “countdown from 10 seconds to 0 (liftoff)” to the serial monitor.

### Countdown Video

[![01_countdown](/thumbs/01_countdown_thumb.png)](https://youtu.be/wBfttG0zpk0)

### Countdown Wiring

There’s no wiring in this assignment. Just plug the pico into the computer.

### Countdown Code

[01_countdown.py](/code/01_countdown.py):

```python
# 2022-09-02, Em Heisig (hheisig51)
# Creates a countdown from 10 seconds to 0 seconds (liftoff) and prints it to the serial monitor.

import time

for x in range(10, 0, -1): # Moves from 10 to 0 in increments of 1
    if x > 0:
        print(f"{x} seconds left!") # prints the number of seconds left
        time.sleep(1)

print(f"Liftoff!") # since x is not greater than 0, this prints
```

### Countdown Reflection

My biggest challenge was figuring out the loop. I first tried making two `while.True()` loops, which didn’t work. Then, I tried using `if` and `else` inside a `while.True()`, which works, albeit clunky. Finally, I got to using a `for` loop, which makes much more sense in this use-case.

## Lights (Launch Pad #2)

### Lights Description

As the countdown ticks down, a red light will blink every second. At 0 seconds (liftoff), a green LED will turn on.

### Lights Video

[![02_lights](/thumbs/02_lights_thumb.png)](https://youtu.be/BNFl4jrQMi0)

### Lights Wiring

![02_lights_wiring](/wiring/02_lights_wiring.png)

### Lights Code

[02_lights.py](/code/02_lights.py):

```python
# 2022-09-09, Em Heisig (hheisig51)
# As the countdown (from 01_countdown.py) ticks down, a red light will blink every second. At 0 seconds (liftoff), a green LED will turn on.

import board
import digitalio
import time

g_led = digitalio.DigitalInOut(board.GP18)
r_led = digitalio.DigitalInOut(board.GP13)
g_led.direction = digitalio.Direction.OUTPUT
r_led.direction = digitalio.Direction.OUTPUT

for x in range(10, 0, -1): # Moves from 10 to 0 in increments of 1
    if x > 0:
        print(f"{x} seconds left!") # Prints the number of seconds left
        r_led.value = True # Turns the red LED on
        time.sleep(.3)
        r_led.value = False # Turns red LED off 0.3 seconds into the 1.0 second cycle.
        time.sleep(.7)

ppschakelrint(f"Liftoff!") # Since x is not greater than 0, this prints
g_led.value = True
time.sleep(2)
g_led.value = False
```

### Lights Reflection

This one was simple. Just remember, the long leg of the LED is the positive leg, and **always use a resistor**. I’ve forgotten that before, and it completely fries your LED.

## Button (Launch Pad #3)

### Button Description

In addition to the previous segments (see 01_countdown.py and 02_lights.py), this assignment adds a button to start the countdown.

### Button Video

[![03_button](/thumbs/03_button_thumb.jpg)](https://youtu.be/kNC3ZjlUSRQ)

### Button Wiring

![03_button_wiring](/wiring/03_button_wiring.png)

### Button Code

[03_button.py](/code/03_button.py)

Let’s import our libraries and set up our LEDs’ like before.

```python
import board
import digitalio
import time

g_led = digitalio.DigitalInOut(board.GP18) # assigns a board.pin (GP18) to a variable (g_led)
r_led = digitalio.DigitalInOut(board.GP13)
g_led.direction = digitalio.Direction.OUTPUT # assigns the variable, with a pin now attached to it, as an output
r_led.direction = digitalio.Direction.OUTPUT
```

Now, we’ll set up the button, as an `INPUT` rather than an `OUTPUT`, and as a [pull-up](https://www.electronics-tutorials.ws/logic/pull-up-resistor.html) resistor.

```python
button = digitalio.DigitalInOut(board.GP16) # see above
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # sets the button to function as a "pull-up" resistor, with a default value of true.
```

Same code as before, except the `for` loop is now nested inside `if butto.value == False:`, making it only trigger when the button is pressed.

```python
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
```

### Button Reflection

Figuring out the difference between a pull-up and a pull-down configuration for the button was very tricky. So, I made this little diagram to help myself out:

|                 | Pull-up | Pull-down |
| --------------- | ------- | --------- |
| Default value   | True    | False     |
| “Pressed” value | False   | True      |
| Wired to        | GND     | 3V3(OUT)  |

It was very frustrating figuring that out. My advice is to ask whatever question you need to ask to actually understand the wiring. Nobody’s going to judge you unless they’re a jerk.

## Servo (Launch Pad #4)

### Servo Description

In addition to the previous segments (see 03_button.py), this assignment adds a servo that simulates “the launch tower disconnecting.” The servo will start at a position of 0 degrees, then move to 180 degrees when “liftoff” is achieved.

### Servo Video

[![04-servo](/thumbs/04_servo_thumb.jpg)](https://youtu.be/Ae4TovFA4m0)

### Servo Wiring

![04_servo.py](/wiring/04_servo_wiring.png)

### Servo Code

[04_servo.py](/code/04_servo.py):

There is some new code relating to the servo, but it’s pretty standard. I recommend looking at the code file and its comments.

### Servo Reflection

This reflection is less about this singular assignment, but more about this Launch Pad assignment as a whole. I think it highlights the importance of segmenting your process when making something. Not fragmenting! You need to make sure things work together. But segmenting, and building one on top of the other, rather than building a servo and a button and lights and a countdown.

## Accelerometer (Crash Avoidance #1)

### Accelerometer Description

This assignment just prints x, y, and z acceleration values from an MPU-6050 chip to the serial monitor.

### Accelerometer Video

[![05_accelerometer](/thumbs/05_accelerometer_thumb.jpg)](https://youtu.be/TKAAT-HO4Mc)

### Accelerometer Wiring

![05_accelerometer-wiring](/wiring/05_accelerometer_wiring.png)

### Accelerometer Code

[05_accelerometer.py](/code/05_accelerometer.py):

```python
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
```

### Accelerometer Reflection

&

## Light and Powerboost (Crash Avoidance #2)

### Light Powerboost Description

In this assignment, a red LED lights up if {x} is within a certain range (Acceleration of 0 to -4, which rougly corresponds with a rotation of 90 degrees).

### Light Powerboost Video

[![06_light-powerboost](/thumbs/06_light-powerboost_thumb.jpg)](https://youtu.be/jTGpdxc1or4)

### Light Powerboost Wiring

![06_light-powerboost_wiring](/wiring/06_light-powerboost_wiring.png)

### Light Powerboost Code

[06_light-powerboost.py](/code/06_light-powerboost.py):

```python
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
```

### Light Powerboost Reflection

&

## OLED (Crash Avoidance #3)

### OLED Description

In addition to the previous assignments, this adds an OLED screen to print the values.

### OLED Video

[![07_oled](/thumbs/07_oled_thumb.jpg)](https://youtu.be/T-bkKQTI-oA)

### OLED Wiring

&

### OLED Code

This assignment is rather long, so I recommend looking at it and its comments at the code file: [07-oled.py](/code/07_oled.py)

### OLED Reflection

&

## Functions (Landing Area #1)

### Functions Description

This assignment takes 6 inputs (of 3 coordinate pairs) and returns the area of their triangle, or returns an error.

### Functions Video

[![08_functions](/thumbs/08_functions_thumb.jpg)](https://youtu.be/5cZ8-UEdc7A)

### Functions Wiring

No wiring was necessary for this assignment. Only the pico was used.

### Functions Code

This assignment is lengthy, as its only code, no wiring. I recomend looking at it in its code file: [08_functions.py](/code/08_functions.py)

### Functions Reflection

&

## Plotting (Landing Area #2)

### Plotting Description

You have successfully written a script to calculate and return the area of each triangle. Now, your commander has asked that you include a small OLED screen to improve visualization of where the landing area is relative to the base.

(Description taken from Paul Schakel ([pschake34](https://github.com/pschake34/Engineering_4_Notebook#landing-area-part-2)), with permission)

### Plotting Video

&

### Plotting Wiring

&

### Plotting Code

&

### Plotting Reflection

&

## Ring and Spinner (CAD #1)

## Key and Prop (CAD #2)

## Assembling the Launcher (CAD #3)

## About

“Somebody is thinking today” - Mr. Miller

Hi! I’m Em Heisig, and I’m a junior at Charlottesville High School. You can reach me at [hheisig51@charlottesvilleschools.org](hheisig51@charlottesvilleschools.org) or [github@eheisig.com](github@eheisig.com).
