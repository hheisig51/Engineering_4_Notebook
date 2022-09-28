# Engineering_4_Notebook

## Table of Contents

- [Pico](#pico)
- [Countdown](#countdown-launch-pad-1)
- [Lights](#lights-launch-pad-2)
- [Button](#button-launch-pad-3)
- [About](#about)

## Pico

These assignments were completed on a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) microcontroller, running [Circuit Python](https://circuitpython.org/board/raspberry_pi_pico/) 7.3.2

## Countdown (Launch Pad #1)

### Countdown Description

The purpose of this assignment is to print a "countdown from 10 seconds to 0 (liftoff)" to the serial monitor.

### Countdown Video

[![Countdown_1](/images/Thumbnail-Countdown_1.png)](https://youtu.be/wBfttG0zpk0)

### Countdown Wiring

There's no wiring in this assignment. Just plug the pico into the computer.

### Countdown Code

[01-countdown.py](/code/01-countdown.py):

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

My biggest challenge was figuring out the loop. I first tried making two `while.True()` loops, which didn't work. Then, I tried using `if` and `else` inside of a `while.True()`, which works, albeit clunk-ily. Finally, I got to using a `for` loop, which makes much more sense in this use-case.

## Lights (Launch Pad #2)

### Lights Description

As the countdown ticks down, a red light will blink every second. At 0 seconds (liftoff), a green LED will turn on.

### Lights Video

[![Lights_2](/images/Thumbnail-Lights_2.png)](https://youtu.be/BNFl4jrQMi0)

### Lights Wiring

![02_lights_wiring](/images/Wiring/02_lights_wiring.png)

### Lights Code

[02-lights.py](/code/02-lights.py):

```python
# 2022-09-09, Em Heisig (hheisig51)
# As the countdown (from 01-countdown.py) ticks down, a red light will blink every second. At 0 seconds (liftoff), a green LED will turn on.

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

This one was simple. Just remember, the long leg of the LED is the positive leg, and **always use a resistor**. I've forgotten that before, and it completely fries your LED.

## Button (Launch Pad #3)

### Button Description

In addition to the previous segments (see 01-countdown.py and 02-lights.py), this assignments adds a button to start the countdown.

### Button Video

[![Button_3](/images/Thumbnail-Button_3.jpg)](https://youtu.be/kNC3ZjlUSRQ)

### Button Wiring

![03_button_wiring](/images/Wiring/03_button_wiring.png)

### Button Code

[03-button.py](/code/03-button.py)

Let's import our libraries and setup our LEDs' like before.

```python
import board
import digitalio
import time

g_led = digitalio.DigitalInOut(board.GP18) # assigns a board.pin (GP18) to a variable (g_led)
r_led = digitalio.DigitalInOut(board.GP13)
g_led.direction = digitalio.Direction.OUTPUT # assigns the variable, with a pin now attached to it, as an output
r_led.direction = digitalio.Direction.OUTPUT
```

Now, we'll setup the button, as an `INPUT` rather than an `OUTPUT`, and as a [pull-up](https://www.electronics-tutorials.ws/logic/pull-up-resistor.html) resistor.

```python
button = digitalio.DigitalInOut(board.GP16) # see above
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # sets the button to function as a "pull-up" resistor, with a default value of true.
```

Same code as before, except the `for` loop is now nested inside of `if butto.value == False:`, making it only trigger when the button is pressed.

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
| "Pressed" value | False   | True      |
| Wired to        | GND     | 3V3(OUT)  |

It was very frustrating figuring that out. My advice is to ask whatever question you need to ask to actually understand the wiring. Nobody's going to judge you unless they're a jerk.

## Servo (Launch Pad #4)

## Servo Description

## Servo Video

[![Servo_4](/images/Thumbnail-Servo_4.jpg)](https://youtu.be/Ae4TovFA4m0)

## Servo Wiring

![04-servo.py](/images/Wiring/04_servo_wiring.png)

## Servo Reflection

## About

"Somebody's thinking today" - Mr. Miller, my teacher

Hi! I'm Em Heisig, and I'm a junior at Charlottesville High School. You can reach me at [hheisig51@charlottesvilleschools.org](hheisig51@charlottesvilleschools.org) or [github@eheisig.com](github@eheisig.com).
