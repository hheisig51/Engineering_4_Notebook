# Engineering_4_Notebook

## Table of Contents

- [Countdown](#countdown-assignment-1)

## Countdown (Assignment #1)

## Countdown Description

The purpose of this assignment is to print a "countdown from 10 seconds to 0 (liftoff)" to the serial monitor.

### Countdown Evidence

[![Countdown-1](/images/Thumbnail_Countdown-1.png)](https://youtu.be/f14LzZC5-tY)

### Countdown Wiring

There's no wiring in this assignment.

### Countdown Code

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
