# 2022-09-02, Em Heisig (hheisig51)

import board
import time

x = 10

for x in range(10, 0, -1):
    if x > 0:
        print(f"{x} seconds left!")
        time.sleep(1)

print(f"Liftoff!")
